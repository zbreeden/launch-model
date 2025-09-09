#!/usr/bin/env python3
import csv, os, requests, sys
from datetime import datetime, timezone

OWNER = "zbreeden"
REPO  = "The-Launch"  # change per repo or loop over a list
OUT   = "data/ops/workflow_runs.csv"
TOKEN = os.getenv("GITHUB_TOKEN")

headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
runs = []
page = 1
while True:
    r = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/actions/runs",
                     params={"per_page": 100, "page": page}, headers=headers, timeout=30)
    if r.status_code != 200: print(r.text); break
    batch = r.json().get("workflow_runs", [])
    if not batch: break
    for x in batch:
        started = x.get("run_started_at") or x.get("created_at")
        completed = x.get("updated_at") if x.get("status")=="completed" else None
        def ts(s): 
            if not s: return None
            return datetime.fromisoformat(s.replace('Z','+00:00'))
        sdt, edt = ts(started), ts(completed)
        duration = int((edt - sdt).total_seconds()) if (sdt and edt) else ""
        runs.append({
            "repo": f"{OWNER}/{REPO}",
            "workflow_name": x.get("name",""),
            "run_id": x.get("id",""),
            "attempt": x.get("run_attempt",""),
            "event": x.get("event",""),
            "actor": (x.get("actor") or {}).get("login",""),
            "branch": (x.get("head_branch") or ""),
            "commit_sha": (x.get("head_sha") or "")[:7],
            "started_at": started or "",
            "completed_at": completed or "",
            "duration_sec": duration,
            "status": x.get("status",""),
            "conclusion": x.get("conclusion",""),
            "queue_time_sec": "",
            "triggered_by": "cron" if x.get("event")=="schedule" else ("git_push" if x.get("event")=="push" else x.get("event","")),
            "url": x.get("html_url",""),
            "logs_url": x.get("logs_url",""),
            "sla_sec": 600,
            "sla_met": str(duration!="" and duration <= 600).lower(),
            "notes": ""
        })
    page += 1

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(runs[0].keys()) if runs else [
        "repo","workflow_name","run_id","attempt","event","actor","branch","commit_sha",
        "started_at","completed_at","duration_sec","status","conclusion","queue_time_sec",
        "triggered_by","url","logs_url","sla_sec","sla_met","notes"
    ])
    w.writeheader()
    w.writerows(runs)
print(f"Wrote {len(runs)} runs → {OUT}")
