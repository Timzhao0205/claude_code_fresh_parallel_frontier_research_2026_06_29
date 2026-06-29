#!/usr/bin/env bash
set -euo pipefail

# Run from repository root.

branches=(
  "frontier-power"
  "frontier-semiconductor"
  "frontier-biomed"
  "frontier-industrial"
  "frontier-extreme"
  "frontier-company-radar"
  "frontier-china-feasibility"
)

dirs=(
  "../frontier-worker-power"
  "../frontier-worker-semiconductor"
  "../frontier-worker-biomed"
  "../frontier-worker-industrial"
  "../frontier-worker-extreme"
  "../frontier-worker-company-radar"
  "../frontier-worker-china-feasibility"
)

for i in "${!branches[@]}"; do
  branch="${branches[$i]}"
  dir="${dirs[$i]}"
  if git worktree list | grep -q "$dir"; then
    echo "Worktree already exists: $dir"
  else
    git worktree add "$dir" -b "$branch"
    echo "Created $dir on branch $branch"
  fi
done

echo "Done. Start Claude in each worktree when ready."
