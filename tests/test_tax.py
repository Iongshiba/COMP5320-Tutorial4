"""Tutorial 4: Unit Testing & Branch Coverage Practice.

Author: Software Engineering Teaching Team
Topic: Unit testing with unittest, Arrange-Act-Assert (AAA), and branch coverage with pytest-cov.

Instructions:
1. Work through the TODOs in order.
2. In Part A, complete tests 1 to 5 to build your initial test suite.
   Run: uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" -v
3. In Part B, run statement coverage, then branch coverage:
   Statement: uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" --cov=src.tax --cov-report=term-missing
   Branch:    uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" --cov=src.tax --cov-branch --cov-report=term-missing
4. Complete tests 6 and 7 to achieve 100% branch coverage!
"""

import unittest

from src.tax import calculate_deduction


class TestCalculateDeduction(unittest.TestCase):
    # =========================================================================
    # PART A: Build the Initial Test Suite
    # Follow the Arrange–Act–Assert (AAA) pattern for each test.
    # =========================================================================

    def test_no_supplements_above_mid_income(self) -> None:
        """WORKED EXAMPLE: Taxpayer earning > $37,000 with no supplements gets $0 deduction."""
        # Arrange
        income = 50_000.0
        age = 40
        has_spouse = False
        disabled = False

        # Act
        result = calculate_deduction(income, age, has_spouse, disabled)

        # Assert
        self.assertIsNotNone(result)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 0.0)

    def test_full_low_income_supplement(self) -> None:
        """TODO 1: Taxpayer earning <= $18,200 qualifies for $700 deduction."""
        self.fail("TODO 1: implement this test")
        # Arrange
        # TODO: Set up inputs where income <= 18_200 (age < 67, has_spouse=False, disabled=False)

        # Act
        # TODO: Call calculate_deduction with the arranged inputs

        # Assert
        # TODO: Assert that result equals 700.0

    def test_senior_supplement(self) -> None:
        """TODO 2: Taxpayer aged >= 67 qualifies for $400 supplement."""
        self.fail("TODO 2: implement this test")
        # Arrange
        # TODO: Set up inputs where age >= 67 (income > 37k, has_spouse=False, disabled=False)

        # Act
        # TODO: Call calculate_deduction with the arranged inputs

        # Assert
        # TODO: Assert that result equals 400.0 (and optionally assertGreater(result, 0))

    def test_spouse_offset(self) -> None:
        """TODO 3: Taxpayer claiming spouse offset qualifies for $200 offset."""
        self.fail("TODO 3: implement this test")
        # Arrange
        # TODO: Set up inputs where only has_spouse is True (income > 37k, age < 67, disabled=False)

        # Act
        # TODO: Call calculate_deduction with the arranged inputs

        # Assert
        # TODO: Assert that result equals 200.0

    def test_disability_supplement(self) -> None:
        """TODO 4: Taxpayer claiming disability supplement qualifies for $600 supplement."""
        self.fail("TODO 4: implement this test")
        # Arrange
        # TODO: Set up inputs where only disabled is True (income > 37k, age < 67, has_spouse=False)

        # Act
        # TODO: Call calculate_deduction with the arranged inputs

        # Assert
        # TODO: Assert that result equals 600.0

    def test_all_supplements_combined(self) -> None:
        """TODO 5: Taxpayer qualifies for every supplement: 700 + 400 + 200 + 600 = 1900."""
        self.fail("TODO 5: implement this test")
        # Arrange
        # TODO: Set up inputs where all supplements apply (income <= 18_200, age >= 67, has_spouse=True, disabled=True)

        # Act
        # TODO: Call calculate_deduction with the arranged inputs

        # Assert
        # TODO: Assert that result is almost equal to 1_900.0 using self.assertAlmostEqual(result, 1_900.0, places=2)

    # =========================================================================
    # PART B: Measure and Close Coverage Gaps
    #
    # 1. Statement coverage:
    #    uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" --cov=src.tax --cov-report=term-missing
    # 2. Branch coverage:
    #    uv run pytest tests/test_tax.py -k "not test_negative and not test_mid" --cov=src.tax --cov-branch --cov-report=term-missing
    #
    # Notice missing lines 27 and 34 in src/tax.py.
    # Complete TODO 6 and TODO 7 below to cover those branches!
    # =========================================================================

    def test_negative_income_raises_value_error(self) -> None:
        """TODO 6: Negative income must raise ValueError('Income cannot be negative')."""
        self.fail("TODO 6: implement this test")
        # Arrange
        # TODO: Set up inputs where income < 0 (e.g., income = -500.0, age = 40, has_spouse=False, disabled=False)

        # Act & Assert
        # TODO: Use with self.assertRaisesRegex(ValueError, "cannot be negative") and call calculate_deduction inside the block

    def test_mid_income_partial_supplement(self) -> None:
        """TODO 7: Income between $18,200 and $37,000 gets $300 supplement."""
        self.fail("TODO 7: implement this test")
        # Arrange
        # TODO: Set up inputs where income is between 18_200 and 37_000 (age < 67, has_spouse=False, disabled=False)

        # Act
        # TODO: Call calculate_deduction with the arranged inputs

        # Assert
        # TODO: Assert that result equals 300.0 (and optionally assertLess(result, 700.0))


if __name__ == "__main__":
    unittest.main()
