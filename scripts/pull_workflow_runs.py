#!/usr/bin/env python3
import csv, os, requests
from datetime import datetime

OWNER = os.getenv("OWNER", "zbreeden")
REPOS = [r.strip() for r in os.getenv("REPOS","The-Launch").split(",") if r.strip()]
OUT   = "data/ops/workflow_runs.csv"
TOKEN = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}

def iso(s): return s.replace('Z','+00:00') if s else None

rows = []
for repo in REPOS:
    page = 1
    while True:
        r = requests.get(
            f"https://api.github.com/repos/{OWNER}/{repo}/actions/runs",
            params={"per_page": 100, "page": page},
            headers=headers, timeout=30
        )
        if r.status_code != 200: break
        batch = r.json().get("workflow_runs", [])
        if not batch: break
        for x in batch:
            started = x.get("run_started_at") or x.get("created_at")
            completed = x.get("updated_at") if x.get("status")=="completed" else ""
            # duration
            try:
                ds = datetime.fromisoformat(iso(started)) if started else None
                de = datetime.fromisoformat(iso(completed)) if completed else None
                dur = int((de - ds).total_seconds()) if (ds and de) else ""
            except Exception:
                dur = ""
            event = x.get("event","")
            sla = 600
            slamet = (isinstance(dur,int) and dur <= sla)
            rows.append({
                "repo": f"{OWNER}/{repo}",
                "workflow_name": x.get("name",""),
                "run_id": x.get("id",""),
                "attempt": x.get("run_attempt",""),
                "event": event,
                "actor": (x.get("actor") or {}).get("login",""),
                "branch": x.get("head_branch") or "",
                "commit_sha": (x.get("head_sha") or "")[:7],
                "started_at": started or "",
                "completed_at": completed or "",
                "duration_sec": dur,
                "status": x.get("status",""),
                "conclusion": x.get("conclusion",""),
                "queue_time_sec": "",
                "triggered_by": "cron" if event=="schedule" else ("git_push" if event=="push" else event),
                "url": x.get("html_url",""),
                "logs_url": x.get("logs_url",""),
                "sla_sec": sla,
                "sla_met": str(slamet).lower(),
                "notes": ""
            })
        page += 1

os.makedirs(os.path.dirname(OUT), exist_ok=True)
fields = ["repo","workflow_name","run_id","attempt","event","actor","branch","commit_sha",
          "started_at","completed_at","duration_sec","status","conclusion","queue_time_sec",
          "triggered_by","url","logs_url","sla_sec","sla_met","notes"]
with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print(f"Wrote {len(rows)} rows from {len(REPOS)} repo(s) → {OUT}")
