# 01 — Install Claude Code

## 1.1 Check your prerequisites

You need:

- A Claude account with access to Claude Code.
- A terminal: macOS Terminal, Windows PowerShell, Linux terminal, or WSL.
- Git.
- Python 3.
- Optional: VS Code.
- Optional: tmux.

## 1.2 Install Claude Code

### macOS / Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Restart the terminal and check:

```bash
claude --version
```

### Windows PowerShell

```powershell
irm https://claude.ai/install.ps1 | iex
```

Restart PowerShell and check:

```powershell
claude --version
```

## 1.3 Log in

Run:

```bash
claude
```

Follow the browser login flow. Inside Claude Code, run:

```text
/status
/help
```

Exit with:

```text
/exit
```

## 1.4 Install Git

Check:

```bash
git --version
```

If missing:

- macOS: install Xcode Command Line Tools or Git from git-scm.com.
- Windows: install Git for Windows.
- Ubuntu/WSL:

```bash
sudo apt update
sudo apt install -y git
```

## 1.5 Check Python

macOS / Linux / WSL:

```bash
python3 --version
```

Windows:

```powershell
python --version
```

## 1.6 Optional: VS Code

Open the project folder later with:

```bash
code .
```

## 1.7 Optional: tmux

macOS:

```bash
brew install tmux
```

Ubuntu / WSL:

```bash
sudo apt update
sudo apt install -y tmux
```

Beginners can skip tmux and use multiple terminal windows.
