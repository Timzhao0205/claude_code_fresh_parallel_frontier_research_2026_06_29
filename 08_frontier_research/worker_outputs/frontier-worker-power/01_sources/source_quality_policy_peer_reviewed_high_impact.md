# Source Quality Policy — Peer-Reviewed / High-Impact Academic Evidence

## Academic evidence rule

Count an academic article only if:

1. It is peer-reviewed; and
2. It is in one of:
   - JCR Q1 or Q2 journal;
   - JIF percentile >= 50;
   - Scopus CiteScore percentile >= 50;
   - SCImago SJR Q1 or Q2;
   - top peer-reviewed conference in the field.

## High-impact label

High impact:
- JCR Q1
- JIF percentile >= 75
- Scopus CiteScore percentile >= 75
- SJR Q1
- top flagship conference

Moderate impact:
- JCR Q2
- JIF percentile 50–75
- Scopus CiteScore percentile 50–75
- SJR Q2
- respected peer-reviewed conference proceedings

Do not count:
- Q3/Q4 journals unless no alternative and explicitly downgraded;
- predatory or unverified journals;
- preprints;
- workshop papers without formal peer review.

## Conference rule

Engineering, robotics, AI, semiconductor, and CS conferences may count if final accepted peer-reviewed proceedings are cited. Label them:

`peer_reviewed_conference_no_jif`

Accepted examples:
- IEEE IEDM
- ISSCC
- VLSI Symposium
- IEEE APEC
- IEEE ECCE
- IEEE ICRA
- IEEE IROS
- RSS
- CoRL
- NeurIPS
- ICML
- ICLR
- CVPR / ICCV / ECCV
- DAC
- CHI
- ASPLOS / ISCA / MICRO / HPCA

## Non-article evidence

Official policy, regulation, standards, government statistics, public filings, procurement records, national-lab technical reports, industry-association statistics, and standards-body documents do not require impact factors. They are valid non-article evidence when directly relevant.

## Evidence statuses

Use exactly:
- CLEARED
- CLEARED_WITH_WEAKNESS
- HOLD
- KILL
- WATCH
- WEAK_SIGNAL_ONLY

## Hard rule

No candidate may be ranked in the top list if its core technical or customer-pain claim is supported only by preprints, company claims, market reports, or weak journalism.
