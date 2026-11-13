# Tutorial 4: Testing Lab Guide

Work through the labs in order. Each lab README includes a presenter demo and
student tasks. Run every terminal command from this repository root
(`COMP5320-Tutorial4/`).

## Quick start

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and use
Python 3.14 or later (the same requirement as the original tutorial).

```bash
uv sync
uv run pytest --version
uv run pytest lab01/test_tax.py::TestCalculateDeduction::test_no_supplements_above_mid_income -v
```

`uv sync` creates `.venv` and installs pytest, pytest-cov and Selenium 4 from the
single root `pyproject.toml` and `uv.lock`. No separate lab environment is needed.

For browser tests, install **Google Chrome** and check that you can open
<https://www.saucedemo.com/>. Selenium Manager finds the browser driver; the first
run may need internet access to download a matching ChromeDriver. Run this once
before class:

```bash
uv run pytest lab02/test_login.py::test_login_success -v
```

The shared `driver` fixture in `conftest.py` opens a **visible Chrome window** for
each test and closes it afterwards, including when an assertion fails. For an
agent or a machine without a display, add `--headless`:

```bash
uv run pytest lab02/test_login.py::test_login_success -v --headless
```

If Chrome, a driver download or the site is blocked, keep the actual error and
retry the same command on a machine with Chrome and network access. A setup error
is not a passing test.
If you already have a matching ChromeDriver, set `SE_CHROMEDRIVER` to its absolute
executable path before running pytest to bypass the automatic driver download.

## Labs

1. [Lab 1: White-box testing](lab01/README.md) — complete seven unit tests and
   measure statement and branch coverage.
2. [Lab 2: Selenium login with pytest](lab02/README.md) — run the login demo and
   write two error tests.
3. [Lab 3: Agentic checkout](lab03/README.md) — use a coding agent to create
   `lab03/test_checkout.py` through browser exploration.
4. [Lab 4: Review the generated test](lab04/README.md) — check that the checkout
   test rejects an order containing the wrong product.

The starter intentionally contains unfinished tests. Lab 1 has seven TODO
failures and Lab 2 has two TODO failures until you implement them. Run the named
demo tests first. `lab03/test_checkout.py` does not exist until Lab 3.

After finishing all exercises and restoring Backpack in Lab 4, check everything:

```bash
uv run pytest lab01 lab02 lab03 -v
```

## Submission

Submit a ZIP of the **whole tutorial folder**, including all four lab folders,
the shared setup files and all tests you completed. Include
**`lab03/test_checkout.py` after the review in Lab 4**.

Name the file exactly **`tutorial4_{Student_Id}.zip`**, replacing `{Student_Id}`
with your student ID. Example: **`tutorial4_V202612345.zip`**.

Exclude `.git`, `.venv`, caches, coverage output and old ZIP files. You can use
your archive tool, or run the following from the repository root after changing
the example student ID:

```bash
uv run python - <<'PY'
import os
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

student_id = "V202612345"  # Replace with your student ID.
root = Path.cwd()
assert (root / "lab03/test_checkout.py").is_file(), "Finish Labs 3 and 4 first"
archive = root / f"tutorial4_{student_id}.zip"
excluded = {".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache",
            ".ruff_cache", ".cache", "htmlcov"}
with ZipFile(archive, "w", ZIP_DEFLATED) as submission:
    for folder, directories, files in os.walk(root):
        directories[:] = [name for name in directories if name not in excluded]
        for name in files:
            if name.lower().endswith(".zip") or name.startswith(".coverage"):
                continue
            if name in {"coverage.json", ".DS_Store"}:
                continue
            path = Path(folder) / name
            submission.write(path, Path(root.name) / path.relative_to(root))
print(archive.name)
PY
```

**Open the ZIP before uploading.** Check that it contains the tutorial folder,
`lab01/`, `lab02/`, `lab03/`, `lab04/`, your completed tests, the README files,
`conftest.py`, `pyproject.toml` and `uv.lock`. In particular, open
`lab03/test_checkout.py` inside the ZIP and confirm that it is the reviewed
version. Check that no `.git`, `.venv`, cache folders or old ZIP files are inside.
