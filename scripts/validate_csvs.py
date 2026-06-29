import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
expected = {
    "03_evidence_ledgers/source_evidence_ledger.csv": ['source_id','worker_id','date_accessed','source_title','source_url_or_citation','domain','source_tier','source_type','peer_reviewed_status','impact_quality','publication_date','geography','topic','claim_supported','direct_support','confidence','limitations','count_toward_evidence','used_in_candidate_ids','notes'],
    "03_evidence_ledgers/source_issue_tracker.csv": ['issue_id','candidate_id','issue_type','issue_summary','required_action','status','notes'],
    "08_frontier_research/frontier_candidate_database.csv": ['candidate_id','domain','candidate_name','one_sentence_product','system_boundary_shift','extreme_metric','first_customer','buyer_title','customer_pain','current_workaround','why_current_solution_fails','hardware_stack','software_stack','prototype_2026_2028','china_wedge','us_wedge','cleanroom_dependency','capex_band','reg_export_risk','competitors','defensibility','kill_criteria','evidence_status','key_sources','worker_id','notes'],
    "08_frontier_research/frontier_scored_database.csv": ['rank','candidate_id','candidate_name','total_score','boundary_shift_score','system_unlock_score','pain_wtp_score','prototype_path_score','hw_sw_depth_score','defensibility_score','china_wedge_score','us_expansion_score','reg_export_inverse_score','capital_efficiency_score','founder_fit_score','evidence_status','decision','notes'],
    "08_frontier_research/company_radar_database.csv": ['company_id','company_name','domain','boundary_shift','extreme_metric','first_market','source_urls','china_analogue_feasibility','adjacent_startup_wedge','why_direct_copy_fails','notes'],
}

ok = True
for rel, header in expected.items():
    path = root / rel
    if not path.exists():
        print(f"MISSING: {rel}")
        ok = False
        continue
    with path.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        actual = next(reader, [])
    if actual != header:
        print(f"HEADER MISMATCH: {rel}")
        print("expected:", header)
        print("actual:  ", actual)
        ok = False
    else:
        print(f"OK: {rel}")

raise SystemExit(0 if ok else 1)
