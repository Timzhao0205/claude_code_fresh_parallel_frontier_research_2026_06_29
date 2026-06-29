# 04 — Numbered Parallel Research Workflow

This is the main operating procedure.

## Phase A — Setup

### 1. Start from the project root

```bash
cd "Fresh Frontier Startup Research 2026-2030"
```

### 2. Check status

```bash
git status
python3 scripts/validate_csvs.py
```

On Windows:

```powershell
python scripts\validate_csvs.py
```

### 3. Run the orchestrator

```bash
claude --model opus --effort xhigh
```

Paste:

```text
Execute prompts/00_orchestrator_parallel_frontier_plan.md exactly. Use CLAUDE.md and the source policies in 01_sources/. Do not rank ideas yet. Build the parallel execution plan and confirm the worker output contract.
```

Save the answer as:

```text
08_frontier_research/merge_outputs/orchestrator_plan.md
```

Commit:

```bash
git add 08_frontier_research/merge_outputs/orchestrator_plan.md
git commit -m "add orchestrator plan"
```

## Phase B — Create parallel worktrees

### 4. Create worktrees

macOS / Linux / WSL:

```bash
bash scripts/create_worktrees.sh
```

Windows PowerShell:

```powershell
.\scripts\create_worktrees.ps1
```

This creates:

```text
../frontier-worker-power
../frontier-worker-semiconductor
../frontier-worker-biomed
../frontier-worker-industrial
../frontier-worker-extreme
../frontier-worker-company-radar
../frontier-worker-china-feasibility
```

## Phase C — Run workers in parallel

Open one terminal per worker.

### 5. Worker 1 — Power

```bash
cd ../frontier-worker-power
claude --model opus --effort xhigh
```

Paste:

```text
Use the frontier-research-worker agent. Execute prompts/01_worker_power_frontier.md. Save the output only to 08_frontier_research/worker_outputs/01_power_frontier.md. Do not edit master CSV files.
```

### 6. Worker 2 — Semiconductor

```bash
cd ../frontier-worker-semiconductor
claude --model opus --effort xhigh
```

Paste:

```text
Use the frontier-research-worker agent. Execute prompts/02_worker_semiconductor_frontier.md. Save the output only to 08_frontier_research/worker_outputs/02_semiconductor_frontier.md. Do not edit master CSV files.
```

### 7. Worker 3 — Biomedical

```bash
cd ../frontier-worker-biomed
claude --model opus --effort xhigh
```

Paste:

```text
Use the frontier-research-worker agent. Execute prompts/03_worker_biomed_frontier.md. Save the output only to 08_frontier_research/worker_outputs/03_biomed_frontier.md. Do not edit master CSV files.
```

### 8. Worker 4 — Industrial

```bash
cd ../frontier-worker-industrial
claude --model opus --effort xhigh
```

Paste:

```text
Use the frontier-research-worker agent. Execute prompts/04_worker_industrial_frontier.md. Save the output only to 08_frontier_research/worker_outputs/04_industrial_frontier.md. Do not edit master CSV files.
```

### 9. Worker 5 — Extreme

```bash
cd ../frontier-worker-extreme
claude --model opus --effort xhigh
```

Paste:

```text
Use the frontier-research-worker agent. Execute prompts/05_worker_extreme_frontier.md. Save the output only to 08_frontier_research/worker_outputs/05_extreme_frontier.md. Do not edit master CSV files.
```

### 10. Worker 6 — US Hinetics-like company radar

```bash
cd ../frontier-worker-company-radar
claude --model opus --effort xhigh
```

Paste:

```text
Use the company-radar-worker agent. Execute prompts/06_worker_us_company_radar.md. Save the output only to 08_frontier_research/worker_outputs/06_us_company_radar.md. Do not edit master CSV files.
```

### 11. Worker 7 — China analogue feasibility

```bash
cd ../frontier-worker-china-feasibility
claude --model opus --effort xhigh
```

Paste:

```text
Use the china-feasibility-analyst agent. Execute prompts/07_worker_china_analogue_feasibility.md. Save the output only to 08_frontier_research/worker_outputs/07_china_analogue_feasibility.md. Do not edit master CSV files.
```

## Phase D — Bring outputs back

### 12. Copy worker outputs into the main folder

If using Git worktrees, easiest method:

```bash
# from each worker worktree, commit output
git add 08_frontier_research/worker_outputs/
git commit -m "worker output"
```

Then in main folder, manually copy or cherry-pick. Simpler beginner method: copy each generated `.md` from each worktree into the main folder's `08_frontier_research/worker_outputs/` directory.

### 13. Merge worker files locally

Main folder:

```bash
python3 scripts/merge_worker_outputs.py
```

Windows:

```powershell
python scripts\merge_worker_outputs.py
```

This creates:

```text
08_frontier_research/merge_outputs/combined_worker_outputs.md
```

## Phase E — Centralized judgment

### 14. Merge and deduplicate

Main folder:

```bash
claude --model opus --effort xhigh
```

Paste:

```text
Use the merger-synthesizer agent. Read 08_frontier_research/merge_outputs/combined_worker_outputs.md. Execute prompts/08_merge_parallel_results.md. Save the result to 08_frontier_research/merge_outputs/parallel_merge.md. Do not score yet.
```

### 15. Source audit

Paste:

```text
Use the peer-reviewed-source-auditor agent. Execute prompts/09_source_audit_peer_reviewed.md against 08_frontier_research/merge_outputs/parallel_merge.md. Save the audit to 08_frontier_research/merge_outputs/source_audit.md. Mark every candidate CLEARED, CLEARED_WITH_WEAKNESS, HOLD, KILL, or WATCH.
```

### 16. Run blocked-source script

```bash
python3 scripts/find_blocked_sources.py
python3 scripts/validate_csvs.py
```

### 17. Score and red-team only cleared candidates

Paste:

```text
Use the red-team-reviewer agent. Execute prompts/10_rank_red_team_frontier.md. Score only candidates marked CLEARED or CLEARED_WITH_WEAKNESS in 08_frontier_research/merge_outputs/source_audit.md. Save the result to 08_frontier_research/merge_outputs/frontier_rank_red_team.md.
```

### 18. China feasibility deep dive

Paste:

```text
Use the china-feasibility-analyst agent. Execute prompts/11_china_feasibility_deep_dive.md for the top 15 candidates in 08_frontier_research/merge_outputs/frontier_rank_red_team.md. Save the result to 08_frontier_research/merge_outputs/china_feasibility_deep_dive.md.
```

### 19. Export final package

Paste:

```text
Execute prompts/13_export_package.md. Produce CSV-ready rows for all databases and a concise session log.
```

### 20. Commit final outputs

```bash
git add .
git commit -m "complete fresh parallel frontier research cycle"
```
