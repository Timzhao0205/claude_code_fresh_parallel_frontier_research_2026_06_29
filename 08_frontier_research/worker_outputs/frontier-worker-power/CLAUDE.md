# Claude Code Instructions — Fresh Parallel Frontier Startup Research

You are operating a fresh from-scratch frontier startup research repository.

## Mission

Find frontier startup ideas in power, semiconductors, biomedical, industrial, and extreme systems. Optimize for Hinetics-like boundary-shifting products, not generic dashboards or conservative procurement-only components.

## Scope

Use these domains:

1. Power / energy / grid / data-center infrastructure
2. Semiconductors / electronics / advanced packaging
3. Biomedical / medtech / bio-instrumentation
4. Industrial / robotics / advanced manufacturing
5. Extreme / cryogenic / superconducting / high-field / harsh environments

## Source rules

Use:

- `01_sources/source_quality_policy_peer_reviewed_high_impact.md`
- `01_sources/source_whitelist_peer_reviewed_high_impact.md`
- `01_sources/source_whitelist_authoritative_non_article.md`
- `01_sources/blocked_sources.md`

Core rules:

- Do not count arXiv, bioRxiv, medRxiv, SSRN, OSF, Research Square, TechRxiv, ChemRxiv, GitHub, Hugging Face, Kaggle, Papers With Code, Medium, Substack, Reddit, or company blogs as academic evidence.
- Academic article evidence must be peer-reviewed and moderate/high impact, preferably JCR Q1/Q2, JIF percentile >=50, Scopus CiteScore percentile >=50, SJR Q1/Q2, or top peer-reviewed conference.
- Official policy, regulation, standards, national-lab reports, government statistics, procurement records, public filings, and industry-association statistics are valid non-article evidence and do not require impact factors.
- Company sources are company claims only.
- Market reports are triangulation only, not customer pain proof.

## Worker rule

Worker sessions may write only to:

`08_frontier_research/worker_outputs/`

Workers must not edit master CSV files.

## Centralized judgment

Only the merger, source auditor, scorer, red-team reviewer, and China feasibility analyst may update:

- `03_evidence_ledgers/source_evidence_ledger.csv`
- `08_frontier_research/frontier_candidate_database.csv`
- `08_frontier_research/frontier_scored_database.csv`
- `08_frontier_research/company_radar_database.csv`

## Candidate quality bar

Every candidate must include:

- One-sentence product
- System boundary shift
- Extreme metric
- First high-end customer
- Buyer title
- Current workaround
- Why current solution fails
- First prototype path 2026–2028
- China feasibility
- US expansion path
- Defensibility
- Kill criteria
- Source evidence

## Idea anti-patterns

Reject:

- Generic AI dashboard
- Monitoring-only tool unless it changes control or treatment
- TAM-only claim
- “China clone of US company” without a defensible wedge
- Cleanroom-heavy idea with no outsourcing path
- Regulatory speculation treated as fact
- Company claim treated as independent evidence

## Final strategy style

Find the engine layer: the subsystem or platform that makes a frontier system possible.
