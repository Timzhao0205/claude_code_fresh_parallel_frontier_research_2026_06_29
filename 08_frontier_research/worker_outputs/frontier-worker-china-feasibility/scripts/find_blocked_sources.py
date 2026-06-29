from pathlib import Path

root = Path(__file__).resolve().parents[1]
blocked_file = root / "01_sources" / "blocked_sources.md"
blocked = []
for line in blocked_file.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if line and not line.startswith('#') and '.' in line and ' ' not in line:
        blocked.append(line.lower())

search_dirs = [root / "08_frontier_research" / "worker_outputs", root / "08_frontier_research" / "merge_outputs"]
found = []
for d in search_dirs:
    for p in d.glob("*.md"):
        text = p.read_text(encoding="utf-8", errors="replace").lower()
        for b in blocked:
            if b in text:
                found.append((p, b))

if found:
    print("Blocked/not-counted source domains found:")
    for p, b in found:
        print(f"- {b} in {p.relative_to(root)}")
    print("These may be weak signals but must not be counted as evidence.")
else:
    print("No blocked domains found in worker/merge markdown outputs.")
