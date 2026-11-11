# Tutorial 4: Lab Guide

## 1. Setup Environment

Open your terminal, navigate into `tutorial4`, and install the dependencies:

```bash
cd tutorial4
uv sync
```

Verify the setup:
```bash
uv run pytest --version
```
Expected: prints `pytest 9.1.1` with plugin `pytest-cov-7.1.0`.

---

## 2. Quick Reference: Rules & Assertions

### Tax Rules (`src/tax.py`)
- `income < 0` $\rightarrow$ raises `ValueError("Income cannot be negative")`
- `income <= 18_200` $\rightarrow$ `+$700`
- `18_200 < income <= 37_000` $\rightarrow$ `+$300`
- `income > 37_000` $\rightarrow$ `+$0`
- `age >= 67` $\rightarrow$ `+$400`
- `has_spouse == True` $\rightarrow$ `+$200`
- `disabled == True` $\rightarrow$ `+$600`

### Unittest Assertions
- `self.assertEqual(result, expected)`
- `self.assertAlmostEqual(result, 1900.0, places=2)`
- `with self.assertRaisesRegex(ValueError, "cannot be negative"):`

---

## 3. Tasks & Expected Outputs

File to edit: `tutorial4/tests/test_tax.py`

### Part A: Initial Test Suite (TODO 1 to 5)

Implement TODO 1 through 5 in `tests/test_tax.py` following the Arrange–Act–Assert pattern.

**Command to run:**
```bash
uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" -v
```

**Expected Output:**
```text
tests/test_tax.py::TestCalculateDeduction::test_no_supplements_above_mid_income PASSED
tests/test_tax.py::TestCalculateDeduction::test_full_low_income_supplement PASSED
tests/test_tax.py::TestCalculateDeduction::test_senior_supplement PASSED
tests/test_tax.py::TestCalculateDeduction::test_spouse_offset PASSED
tests/test_tax.py::TestCalculateDeduction::test_disability_supplement PASSED
tests/test_tax.py::TestCalculateDeduction::test_all_supplements_combined PASSED
============================== 6 passed in 0.XXs ==============================
```

---

### Part B: Measure and Close Coverage Gaps (TODO 6 & 7)

#### Step 1: Statement Coverage
Measures which statements in `src/tax.py` are executed.

**Command to run:**
```bash
uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" --cov=src --cov-report=term-missing -q
```

**Expected Output:**
```text
Name         Stmts   Miss  Cover   Missing
------------------------------------------
src/tax.py      18      2    89%   27, 34
------------------------------------------
TOTAL           18      2    89%
```
- Lines **27** (`raise ValueError`) and **34** (`deduction += 300.0`) are never executed.

#### Step 2: Branch Coverage
Checks whether every decision condition was exercised in **both** True and False directions.

**Command to run:**
```bash
uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" --cov=src --cov-branch --cov-report=term-missing -q
```

**Expected Output:**
```text
Name         Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------
src/tax.py      18      2     12      2    87%   27, 34
--------------------------------------------------------
TOTAL           18      2     12      2    87%
```
- `Branch = 12`: Total decision branches (6 conditions × 2).
- `BrPart = 2`: Two branches were only executed in one direction.

#### Step 3: Implement Missing Tests (TODO 6 & 7)
- **TODO 6 (`test_negative_income_raises_value_error`)**: Test `income < 0` using `with self.assertRaisesRegex(ValueError, "cannot be negative"):`.
- **TODO 7 (`test_mid_income_partial_supplement`)**: Test income between `18_200` and `37_000` (e.g. `25_000.0`) expecting `300.0`.

#### Step 4: Verify 100% Branch Coverage
**Command to run:**
```bash
uv run pytest tests/test_tax.py --cov=src --cov-branch --cov-report=term-missing -q
```

**Expected Output:**
```text
Name         Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------
src/tax.py      18      0     12      0   100%
--------------------------------------------------------
TOTAL           18      0     12      0   100%
8 passed in 0.XXs
```

---

## 4. Submission

From the `tutorial4/` directory, zip `tests/test_tax.py`:

```bash
zip submission.zip tests/test_tax.py
```

**What to submit:**
- `submission.zip` containing `tests/test_tax.py` (or upload `tests/test_tax.py` directly).
