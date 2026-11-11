# Chapter 4: Software Quality & Testing (setup before class)

Please do this **before the lesson**. It takes about 10 minutes and needs an internet connection.
In class we'll use the time for testing, not installing.

We're following *Agentic Software Engineering: A Practical Guide for the AI-Native Engineer*:

- Lecture: <https://book.agentic-swe.dev/chapter_4.html>
- Lab: <https://book.agentic-swe.dev/tutorial_4.html>

## What's in this repo

```
chapter4-software-testing/
├── chapter4/      lecture examples: src/calculator.py and its tests
└── tutorial4/     the lab: src/tax.py is the code you'll test
    └── tests/     empty for now; you'll write test_tax.py here in Part A
```

Each of the two folders is its own small Python project. You set up each one separately.

## 1. Install git and uv

[uv](https://docs.astral.sh/uv/) installs Python, pytest and pytest-cov for you, so you
**don't need to install Python yourself.**

**Windows** (PowerShell):

```powershell
winget install --id Git.Git -e
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS** (Terminal): run `git --version`. If git is missing, macOS offers to install it, so
accept. Then:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Linux**: install git with your package manager if `git --version` doesn't work, then run the
same `curl` command as macOS.

Then **close the terminal and open a new one**, and check:

```
git --version
uv --version
```

If you already had uv, update it with `uv self update`. If you installed it with Homebrew or
winget, use `brew upgrade uv` or `winget upgrade astral-sh.uv` instead.

## 2. Get the code and set up both projects

Open a terminal in the folder where you keep your coursework (your Desktop is fine), then run:

```
git clone https://github.com/phnam05/chapter4-software-testing.git
cd chapter4-software-testing/tutorial4
uv sync
cd ../chapter4
uv sync
```

The first `uv sync` may take a minute. It downloads Python 3.14 (or newer) if you don't have
it, creates a `.venv` folder inside the project, and installs pytest 9.1.1 and pytest-cov 7.1.0.

> **Can't install git?** On the [repo page](https://github.com/phnam05/chapter4-software-testing),
> click **Code → Download ZIP** and unzip it. The folder will be called
> `chapter4-software-testing-main`. `cd` into it and continue from `cd tutorial4`.

## 3. Check that it works

From inside `tutorial4`:

```
uv run python -c "from src.tax import calculate_deduction; print(calculate_deduction(15_000, 40, False, False))"
```

should print `700.0`, and

```
uv run pytest -VV
```

should print `This is pytest version 9.1.1` and list `pytest-cov-7.1.0` under
*registered third-party plugins*.

From inside `chapter4`:

```
uv run python -c "from src.calculator import divide; print(divide(10, 2))"
```

should print `5.0`.

If all three checks give the expected output, you're ready for class.

## Running the book's commands

The book writes commands like `pytest tests/test_tax.py -v`. Type them with **`uv run` in
front**, from inside the project folder (`tutorial4` for the lab):

```
uv run pytest tests/test_tax.py -v
uv run pytest tests/test_tax.py --cov=src --cov-branch --cov-report=term-missing -q
```

`uv run` uses the project's `.venv` automatically, so you never need to "activate" anything.
In lab Part B, Step 1 (`uv add --dev pytest-cov`) will just confirm that pytest-cov is already
installed. That's expected.

On Windows the coverage report prints paths as `src\tax.py` instead of `src/tax.py`. That's
normal.

## Using an editor (optional)

A terminal is all you need. If you use PyCharm or VS Code:

- Open **`tutorial4` itself** as the project, not the `chapter4-software-testing` folder above
  it. Otherwise `from src.tax import ...` won't be found.
- Set the project's Python interpreter to the existing **`.venv`** inside that folder, which
  `uv sync` created. In VS Code, use **Python: Select Interpreter** from the command palette
  (Ctrl/Cmd+Shift+P).

## Troubleshooting

| You see | Fix |
|---|---|
| `git` or `uv`: `command not found` / `is not recognized` | Close the terminal and open a new one. If that doesn't help, restart your computer so the new PATH is picked up. |
| `error: Failed to spawn: pytest` | You're not inside a project folder. `cd` into `tutorial4` (or `chapter4`) first. |
| `ModuleNotFoundError: No module named 'src'` | Same cause: run commands from inside `tutorial4` or `chapter4`, and start them with `uv run`. |
| `git clone` or `uv sync` fails while downloading | You need internet the first time. Campus or corporate networks sometimes block downloads, so try from home or a phone hotspot. |
| PowerShell says running scripts is disabled when you try `.venv\Scripts\Activate.ps1` | You don't need to activate. Use `uv run ...` instead. |

Still stuck? Bring your laptop a few minutes early, along with the exact error message
(a screenshot is fine).
