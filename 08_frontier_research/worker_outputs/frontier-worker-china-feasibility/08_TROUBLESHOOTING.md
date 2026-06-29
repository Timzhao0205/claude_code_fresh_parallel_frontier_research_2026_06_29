# 08 — Troubleshooting

## Claude Code cannot see files

Run:

```text
/memory
```

Check that `CLAUDE.md` is loaded. Ask Claude:

```text
List the files in the project root and confirm you can read prompts/00_orchestrator_parallel_frontier_plan.md.
```

## Claude Code cannot browse

Use Claude Web Research for the worker step. Save the answer into the corresponding worker output file, then return to Claude Code for merge/audit/scoring.

## Worker edits master CSV files

Revert the edits:

```bash
git checkout -- 03_evidence_ledgers/source_evidence_ledger.csv
```

Then rerun the worker with stricter instruction:

```text
Do not edit any CSV. Save only to 08_frontier_research/worker_outputs/[worker].md.
```

## Worktree conflict

List worktrees:

```bash
git worktree list
```

Remove one:

```bash
git worktree remove ../frontier-worker-power
```

Use `--force` only if you are sure you do not need uncommitted changes.

## Claude produces arXiv citations

Tell Claude:

```text
arXiv is blocked as counted evidence. Replace every arXiv citation with a peer-reviewed final journal/conference paper, official standard, or government/national-lab source. If no replacement exists, mark the claim as WEAK_SIGNAL_ONLY.
```
