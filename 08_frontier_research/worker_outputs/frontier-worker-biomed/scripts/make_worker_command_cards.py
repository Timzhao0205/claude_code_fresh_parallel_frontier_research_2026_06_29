from pathlib import Path
root = Path(__file__).resolve().parents[1]
commands = {
"power": "Use the frontier-research-worker agent. Execute prompts/01_worker_power_frontier.md. Save the output only to 08_frontier_research/worker_outputs/01_power_frontier.md. Do not edit master CSV files.",
"semiconductor": "Use the frontier-research-worker agent. Execute prompts/02_worker_semiconductor_frontier.md. Save the output only to 08_frontier_research/worker_outputs/02_semiconductor_frontier.md. Do not edit master CSV files.",
"biomed": "Use the frontier-research-worker agent. Execute prompts/03_worker_biomed_frontier.md. Save the output only to 08_frontier_research/worker_outputs/03_biomed_frontier.md. Do not edit master CSV files.",
"industrial": "Use the frontier-research-worker agent. Execute prompts/04_worker_industrial_frontier.md. Save the output only to 08_frontier_research/worker_outputs/04_industrial_frontier.md. Do not edit master CSV files.",
"extreme": "Use the frontier-research-worker agent. Execute prompts/05_worker_extreme_frontier.md. Save the output only to 08_frontier_research/worker_outputs/05_extreme_frontier.md. Do not edit master CSV files.",
"company_radar": "Use the company-radar-worker agent. Execute prompts/06_worker_us_company_radar.md. Save the output only to 08_frontier_research/worker_outputs/06_us_company_radar.md. Do not edit master CSV files.",
"china_feasibility": "Use the china-feasibility-analyst agent. Execute prompts/07_worker_china_analogue_feasibility.md. Save the output only to 08_frontier_research/worker_outputs/07_china_analogue_feasibility.md. Do not edit master CSV files."
}
out_dir = root / "worker_command_cards"
out_dir.mkdir(exist_ok=True)
for name, cmd in commands.items():
    (out_dir / f"{name}.txt").write_text(cmd, encoding="utf-8")
print(f"Wrote {len(commands)} command cards to {out_dir}")
