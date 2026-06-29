# Prompt 09 — Strict Source Audit: Peer-Reviewed / High-Quality Evidence

## Task
Audit every source and every candidate from the merged output.

## Source policy

Use:

- `01_sources/source_quality_policy_peer_reviewed_high_impact.md`
- `01_sources/source_whitelist_peer_reviewed_high_impact.md`
- `01_sources/source_whitelist_authoritative_non_article.md`
- `01_sources/blocked_sources.md`

## Audit table columns

- candidate_id
- candidate_name
- core technical claim
- core customer-pain claim
- core policy/regulatory claim
- source supporting technical claim
- source supporting customer-pain claim
- source supporting policy/regulatory claim
- source tier
- peer-reviewed status
- impact quality
- direct support: yes/no/partial
- evidence status: CLEARED / CLEARED_WITH_WEAKNESS / HOLD / KILL / WATCH / WEAK_SIGNAL_ONLY
- required repair

## Rules

- arXiv/preprints do not count.
- Company pages do not count as independent proof.
- Market reports do not prove customer pain.
- If a candidate has no direct Tier 1/2 or peer-reviewed/official evidence for its core claim, mark HOLD or WEAK_SIGNAL_ONLY.
- If the idea is generic or impossible to defend, mark KILL.

## Deliverables

1. Full source-audit memo.
2. Cleared candidate list.
3. Hold list.
4. Kill list.
5. Source-repair list.
6. CSV-ready issue tracker rows.
7. CSV-ready updated evidence-ledger rows.
