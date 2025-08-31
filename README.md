# FourTwenty • The Launch

>>Launch templates meant to provide rigid structure, discipline, and constraint foundation needed for good quality data analysis.

Step 1 -> Seed a .yaml

This launch scroll will provide a starter seed, but the premise here is machine readable QA.  GIGO is to be avoided at all cost, and the cleanest way to do this is via technology.  We can define the bias through our guardrails.  It is key to let schematics drive everything, the let humans generate the UI and human readable documents from these specifications.

##Garbage-In-Garbage-Out (GIGO) Guardrails ->
Input contract first
Keep schema.yaml the source of truth for types/ranges/enums.
Add required + pattern (IDs, dates), min/max (rates in 0–1).
Source provenance
Every dataset gets a header: source, extracted_at, row_count, hash.
If you aggregate, record inputs + transform version.
Deterministic validation (fail fast)
Unique keys (no dup IDs, no dup sprints).
Range checks (e.g., onTime ∈ [0,1], no negative counts).
Referential checks (compliance tags ∈ allowed list).
Time sanity (no future dates, no “release before sprint”).
Funnel logic checks
Steps must exist in funnel_spec.yaml.
Transitions must be legal (no started → submitted skips).
SLA timers present when required (e.g., status visible ≤15m).
Anomaly flags, not just errors
Z-score/percentile outlier flags on metrics (warn, don’t fail).
Distribution drift (compare to last archive snapshot).
Sampling + reality checks
Random 20-row sample to eyeball after each ingest.
“Red-team” tests: assert at least 1 record hits each funnel step weekly.
Append-only archive
Snapshots are write-once; supersede with versions, don’t overwrite.
MANIFEST with hashes to prove immutability.
Small, loud CI
Block merge on deterministic failures.
Post warnings as a PR comment (don’t block, but make them visible).
Human note box
A tiny qa/notes.md where you log “known weirdness” (e.g., vendor outage 2025-08-29).
Feedback loop
When a check catches real rot twice, promote it from warn → error.
When a check creates noise, tighten the rule or downgrade it.

--> seed.yaml

version: 1.0.0
meta: { project: "GECU – The Bank", owner: "Zach Breeden", updated: "2025-08-30" }
ui: { thresholds: { wip_max: 5, on_time_target: 0.85 }, tabs: [delivery, traceability, risk] }

initiatives:
  - { id: ACH-01, name: "ACH Dispute Experience", type: Compliance, reg: "Reg E" }
  - { id: LN-01,  name: "Loan App Funnel",       type: Lending,    reg: "GLBA" }

deliveryFlow:
  - { sprint: S-1, wip: 6, throughput: 5, leadTime: 9, cycleTime: 5, onTime: 0.60, defects: 2 }
  - { sprint: S-2, wip: 5, throughput: 6, leadTime: 8, cycleTime: 4, onTime: 0.70, defects: 1 }
  - { sprint: S-3, wip: 5, throughput: 7, leadTime: 7, cycleTime: 4, onTime: 0.82, defects: 1 }
  - { sprint: S-4, wip: 4, throughput: 7, leadTime: 6, cycleTime: 3, onTime: 0.86, defects: 0 }

traceability:
  - epic: "ACH Dispute Status"
    story: "As a member, I can see dispute status in app"
    ac:
      - "Given a dispute exists, When I open it, Then I see current step"
      - "Status reflects backend state within 15 minutes"
    tests: ["API returns state", "UI shows step chips"]
    dataImpact: "fact_dispute_status; join on member_id"
    compliance: "Reg E"
    owner: "ZB"
    status: "Released S-3"
    releaseId: "2025.08.15"

risks:
  - { kind: Risk, item: "PII exposure in exports", impact: High, likelihood: Medium,
      mitigation: "Mask fields; RBAC; audit log", owner: ZB, date: "2025-08-28", next: "2025-09-02" }


STEP 2 -> The following provides an initial README.md seeding for every module birth.  Upon conception, this is step one when buildig the architecture of any decision model.

---
# <GLYPH> -> Project Name -> The ...

## Purpose
- Problem:
- Audience:
- Outcomes (measurable): <e.g., lead time ↓20%, on-time % ≥85%>

## Deliverables (MVP)
1) Delivery Readiness dashboard
2) Requirements→Release traceability
3) Risk & Decision log

## Data Contract (from seed.yaml)
- Entities: initiatives, deliveryFlow, traceability, risks
- IDs must be stable, strings.
- Dates are ISO `YYYY-MM-DD`. Percentages are decimals (0–1).

## UX/KPI Requirements
- Tabs: Delivery | Traceability | Risks
- Charts: Throughput (bar), Lead/Cycle (line)
- Tables: traceability columns = epic, story, ac[], tests[], dataImpact, compliance, owner, status, releaseId
- Accessibility: keyboard navigable, sensible aria labels.

## Non-Goals (for now)
- Live backend
- Auth
- Write APIs

## Definition of Done
- Renders from `seed.yaml` only (no hard-coded data)
- Type-checked props
- README updated with run steps
- Lint clean

## Run
```bash
npm install
npm run dev
