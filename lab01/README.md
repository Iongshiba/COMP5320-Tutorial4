# Lab 1: White-box testing

## Goal and setup

Use Arrange–Act–Assert (AAA) to test `calculate_deduction`, then use statement and
branch coverage to find missing cases. This function uses the classroom rules
below; it is a testing exercise.

Open a terminal at the repository root and install the shared environment:

```bash
uv sync
```

Chrome is not needed for this lab. Read `lab01/tax.py`; edit only
**`lab01/test_tax.py`**. Keep the worked example and implement TODO 1–7.
Remove each `self.fail("TODO ...")` when you implement that test.

## Deduction rules

| Condition | Result |
| --- | --- |
| `income < 0` | Raise `ValueError("Income cannot be negative")` |
| `0 <= income <= 18_200` | Add 700 |
| `18_200 < income <= 37_000` | Add 300 |
| `income > 37_000` | Add 0 for income |
| `age >= 67` | Add 400 |
| `has_spouse` is true | Add 200 |
| `disabled` is true | Add 600 |

The age, spouse and disability amounts add to the income amount.

## Presenter demo

1. Open `lab01/tax.py` and explain the rules and decisions.
2. Open the worked example `test_no_supplements_above_mid_income`. Explain
   **Arrange** (inputs), **Act** (call the function) and **Assert** (check 0.0).
3. Run only that test:

   ```bash
   uv run pytest lab01/test_tax.py::TestCalculateDeduction::test_no_supplements_above_mid_income -v
   ```

   Expected in the starter: **1 passed**.
4. Show a coverage report for the same example:

   ```bash
   uv run pytest lab01/test_tax.py::TestCalculateDeduction::test_no_supplements_above_mid_income --cov=lab01.tax --cov-report=term-missing -q
   ```

   Explain `Stmts` (statements), `Miss` (unexecuted statements), `Cover` and
   **`Missing`** (the source line numbers to inspect in `lab01/tax.py`). The
   example alone leaves several lines missing. A passing test does not mean
   that all decisions were exercised.

## Student practice: TODO 1–5

Follow AAA and the hints in `lab01/test_tax.py`:

| TODO | Test case | Expected deduction |
| --- | --- | --- |
| 1 | Low income, no other supplements | 700.0 |
| 2 | Senior, income above 37,000, no other supplements | 400.0 |
| 3 | Spouse only, income above 37,000, age below 67 | 200.0 |
| 4 | Disability only, income above 37,000, age below 67 | 600.0 |
| 5 | Low income and all supplements | 1900.0 |

Useful assertions: `self.assertEqual(result, expected)` and
`self.assertAlmostEqual(result, 1_900.0, places=2)`.

After completing **only TODO 1–5**, run the worked example and those five tests:

```bash
uv run pytest lab01/test_tax.py -k "not test_negative and not test_mid" -v
```

Expected at this step: **6 passed, 2 deselected**. TODO 6–7 are still unfinished.

## Student practice: find the two gaps

First measure **statement coverage** after TODO 1–5:

```bash
uv run pytest lab01/test_tax.py -k "not test_negative and not test_mid" --cov=lab01.tax --cov-report=term-missing -q
```

Expected at this step (timings and spacing may differ):

```text
Name           Stmts   Miss  Cover   Missing
-------------------------------------------
lab01/tax.py      18      2    89%   27, 34
```

Then measure **branch coverage** for the same six tests:

```bash
uv run pytest lab01/test_tax.py -k "not test_negative and not test_mid" --cov=lab01.tax --cov-branch --cov-report=term-missing -q
```

Expected after TODO 1–5:

```text
Name           Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------
lab01/tax.py      18      2     12      2    87%   27, 34
```

There are six decisions with two outcomes each (`Branch = 12`). Two decisions
have only one tested outcome (`BrPart = 2`). Inspect `Missing`: line 27 raises
for negative income, and line 34 adds the middle-income amount. These gaps tell
you which inputs to add next. Use the current report if source line numbers change.

## Student practice: TODO 6–7 and final check

- **TODO 6:** Use negative income, such as -500.0. Use
  `with self.assertRaisesRegex(ValueError, "cannot be negative"):` and call
  `calculate_deduction` inside that block.
- **TODO 7:** Use income 25,000.0, age below 67 and no other supplements.
  Assert that the result is 300.0.

After completing **all seven TODOs**, measure both kinds of coverage again:

```bash
uv run pytest lab01/test_tax.py --cov=lab01.tax --cov-report=term-missing -q
uv run pytest lab01/test_tax.py --cov=lab01.tax --cov-branch --cov-report=term-missing -q
```

Expected statement report: **18 statements, 0 missed, 100%**.
Expected branch report:

```text
Name           Stmts   Miss Branch BrPart  Cover   Missing
--------------------------------------------------------
lab01/tax.py      18      0     12      0   100%
8 passed
```

These 100% results describe the completed exercise, not the starter. In the
starter, running the whole file reports **1 passed and 7 TODO failures**.
Keep your completed tests for submission.
