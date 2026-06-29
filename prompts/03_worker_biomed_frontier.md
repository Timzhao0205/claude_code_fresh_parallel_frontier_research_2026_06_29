# Prompt 03 — Worker Biomedical Frontier


## Universal worker rules

You are doing fresh deep research from scratch. Do not use old RIDs, old source ledgers, or old rankings.

Use source policies from `01_sources/`:
- peer-reviewed / moderate-high-impact academic sources only for academic article evidence;
- official policy/regulation/standards/national-lab/procurement/public-filing sources for non-article evidence;
- no arXiv/preprints counted;
- company pages are company claims only;
- market reports are triangulation only.

For every candidate, include:
- candidate_id using your worker prefix;
- candidate name;
- one-sentence product;
- system boundary shift;
- extreme metric;
- first high-end customer;
- buyer title;
- pain;
- current workaround;
- why current solution fails;
- hardware stack;
- software/control stack;
- prototype path 2026–2028;
- China wedge;
- US wedge;
- cleanroom dependency;
- capex band;
- regulatory/export risk;
- competitors;
- defensibility;
- kill criteria;
- evidence status;
- key sources.

Output must include:
1. Domain thesis.
2. 20–30 candidate ideas.
3. 20–30 source rows.
4. 3–10 rejected ideas.
5. Top 5 from your worker lane.
6. CSV-ready candidate rows.
7. CSV-ready evidence ledger rows.

Save output only to worker_outputs. Do not edit master CSV files.


## Worker prefix
BIO

## Domain
Biomedical / medtech / bio-instrumentation

## Search topics

- intervention hardware, not monitoring-only devices
- surgical force-control hardware
- robotic catheter or endoluminal actuation
- implantable power / hermetic packaging / neural interfaces
- BCI platforms and subsystems
- organ-on-chip if it changes drug-development workflows
- high-end clinical instrumentation with hardware moat
- closed-loop sensing and therapy systems
- China high-end medical device localization and NMPA constraints
- FDA pathway and reimbursement gates


## Output file
Save your final response to:

```text
08_frontier_research/worker_outputs/03_biomed_frontier.md
```

## Candidate style
Optimize for frontier flagship ideas, not conservative component procurement alone. Search for the engine layer: the subsystem/platform that makes a new high-end system possible.
