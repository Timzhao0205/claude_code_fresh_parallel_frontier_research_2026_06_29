# 05 — Claude Web Research vs Claude Code

Use both when useful.

## Use Claude Code for

- Local folder setup
- Git worktrees
- Parallel worker orchestration
- Writing Markdown outputs
- Maintaining CSV ledgers
- Merge and deduplication
- Source-audit bookkeeping
- Red-team and scoring prompts

## Use Claude Web Research for

- Live web search with citations
- Reading current company pages
- Reading recent policy pages
- Finding current peer-reviewed papers
- Searching official government and standards sources

## Hybrid fallback rule

If a Claude Code worker cannot browse or cannot produce reliable citations, stop that worker and run the same worker prompt in Claude Web Research. Then save the Claude Web answer into the corresponding worker output file.

Example:

```text
Run prompts/01_worker_power_frontier.md in Claude Web Research with Web Search enabled. Save the answer to 08_frontier_research/worker_outputs/01_power_frontier.md.
```

Then return to Claude Code for merge, audit, and scoring.
