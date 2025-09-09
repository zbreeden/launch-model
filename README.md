# FourTwenty • The Launch <seed.README.md>

>>Operational launch templates meant to provide rigid structure, discipline, and constraint foundation needed for good quality data analysis.

##Master Scaffolding
           
/<launch>-model/ | Semantics are important in a machine tagging system
README.md | Scrolls written like journals start to narrate machine code thus making things practical, more stakeholder friendly
index.html | Dashboards need a face
seeds.glossary.yml |
seeds.tags.yml |
seeds.seedset.yml |
seeds.emoji_palette.yml | Image can be just as powerful when tagging
seeds.registry.yml |
seeds.statuses.yml | 
seeds.orbits.yml |
seeds.modules.yml |
signals.latest.json |

Step 1 -> Move seeds/ from main repository...

This launch scroll will provide a starter seedset, but the premise here is machine readable QA.  GIGO is to be avoided at all cost, and the cleanest way to do this is via technology.  We can define the bias through our guardrails.  It is key to let schematics drive everything, then let humans generate the UI and human readable documents from these specifications.


##Garbage-In-Garbage-Out (GIGO) Guardrails --------> qa/rules.yaml
1) Input contract first
- Keep schema.yaml the source of truth for types/ranges/enums.
- Add required + pattern (IDs, dates), min/max (rates in 0–1).

2) Source provenance
- Every dataset gets a header: source, extracted_at, row_count, hash.
- If you aggregate, record inputs + transform version.

3) Deterministic validation (fail fast)
- Unique keys (no dup IDs, no dup sprints).
- Range checks (e.g., onTime ∈ [0,1], no negative counts).
- Referential checks (compliance tags ∈ allowed list).
- Time sanity (no future dates, no “release before sprint”).

4) Funnel logic checks
- Steps must exist in funnel_spec.yaml.
- Transitions must be legal (no started → submitted skips).
- SLA timers present when required (e.g., status visible ≤15m).

5) Anomaly flags, not just errors
- Z-score/percentile outlier flags on metrics (warn, don’t fail).
- Distribution drift (compare to last archive snapshot).

6) Sampling + reality checks
- Random 20-row sample to eyeball after each ingest.
- “Red-team” tests: assert at least 1 record hits each funnel step weekly.

7) Append-only archive
- Snapshots are write-once; supersede with versions, don’t overwrite.
- MANIFEST with hashes to prove immutability.

8) Small, loud CI
- Block merge on deterministic failures.
- Post warnings as a PR comment (don’t block, but make them visible).

9) Human note box
- A tiny qa/notes.md where you log “known weirdness” (e.g., vendor outage 2025-08-29).

10) Feedback loop
- When a check catches real rot twice, promote it from warn → error.
- When a check creates noise, tighten the rule or downgrade it.
