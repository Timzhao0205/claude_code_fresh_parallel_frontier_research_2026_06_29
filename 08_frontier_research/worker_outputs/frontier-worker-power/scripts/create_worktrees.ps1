$branches = @(
  "frontier-power",
  "frontier-semiconductor",
  "frontier-biomed",
  "frontier-industrial",
  "frontier-extreme",
  "frontier-company-radar",
  "frontier-china-feasibility"
)

$dirs = @(
  "..\frontier-worker-power",
  "..\frontier-worker-semiconductor",
  "..\frontier-worker-biomed",
  "..\frontier-worker-industrial",
  "..\frontier-worker-extreme",
  "..\frontier-worker-company-radar",
  "..\frontier-worker-china-feasibility"
)

for ($i = 0; $i -lt $branches.Length; $i++) {
    $branch = $branches[$i]
    $dir = $dirs[$i]
    git worktree add $dir -b $branch
}

Write-Host "Done. Start Claude in each worktree when ready."
