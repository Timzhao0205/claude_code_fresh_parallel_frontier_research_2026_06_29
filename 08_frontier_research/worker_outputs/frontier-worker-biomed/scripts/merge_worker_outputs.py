from pathlib import Path

root = Path(__file__).resolve().parents[1]
worker_dir = root / "08_frontier_research" / "worker_outputs"
out_dir = root / "08_frontier_research" / "merge_outputs"
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "combined_worker_outputs.md"

parts = []
for p in sorted(worker_dir.glob("*.md")):
    if p.name.lower() == "readme.md":
        continue
    parts.append(f"\n\n# FILE: {p.name}\n\n")
    parts.append(p.read_text(encoding="utf-8", errors="replace"))

out_file.write_text("".join(parts), encoding="utf-8")
print(f"Merged {len(parts)//2} worker files into {out_file}")
