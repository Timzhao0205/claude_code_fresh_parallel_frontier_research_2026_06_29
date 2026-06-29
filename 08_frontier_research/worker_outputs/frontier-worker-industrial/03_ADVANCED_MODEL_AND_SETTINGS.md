# 03 — Advanced Model and Settings

## 3.1 Recommended model settings

For frontier research, source audit, merge, and final red-team, use:

```bash
claude --model opus --effort xhigh
```

Inside Claude Code, you can also run:

```text
/model opus
/effort xhigh
```

Use `/effort max` only once for the final top-5 strategy decision. It is expensive and can overthink.

## 3.2 Optional long-context mode

If your Claude Code account supports long context, you can try:

```text
/model opus[1m]
```

Use this for merge and source audit only, not every worker.

## 3.3 Copy the settings file

macOS / Linux / WSL:

```bash
cp .claude/settings.local.example.json .claude/settings.local.json
```

Windows PowerShell:

```powershell
Copy-Item .claude\settings.local.example.json .claude\settings.local.json
```

## 3.4 Verify memory loading

Start Claude Code:

```bash
claude --model opus --effort xhigh
```

Then run:

```text
/memory
```

Confirm that `CLAUDE.md` is loaded.

## 3.5 Verify permissions

Run:

```text
/permissions
```

Keep permissions conservative at first. Do not enable broad auto-approval. You want Claude to ask before destructive file operations.

## 3.6 Important safety rule

Claude Code can edit files. This is useful, but risky. Do not allow it to edit master CSVs from worker sessions. Workers must write only to:

```text
08_frontier_research/worker_outputs/
```

Only the merger/auditor/scorer should update databases.
