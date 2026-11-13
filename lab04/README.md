# Lab 4: Review the generated checkout test

## Goal and setup

Review **`lab03/test_checkout.py`** from Lab 3 on
<https://www.saucedemo.com/>. Can the test detect **successful checkout with the
wrong product**? The requirement stays the same: order **exactly one Sauce Labs
Backpack**.

Complete Lab 3 first. Install Google Chrome and run from the repository root:

```bash
uv sync
uv run pytest lab03/test_checkout.py -v
```

Reuse the `driver` fixture in `conftest.py`. It opens a fresh visible Chrome
session for every run, so the cart starts clean. Add `--headless` to any pytest
command here if your agent environment has no display. If browser startup or
site access fails, fix that first: it does not demonstrate a product assertion.

Final file to edit and submit: **`lab03/test_checkout.py`**. Lab 4 does not create
a separate submission test.

## Presenter demo: a weak assertion

1. Make a temporary copy of the generated test inside the repo so it still
   finds the shared fixture:

   ```bash
   cp lab03/test_checkout.py lab04/test_checkout_demo.py
   ```

2. Edit only this copy for the demo. Keep login, checkout actions, waits and
   the final assertion that checks `Thank you for your order!`. Temporarily
   remove product or quantity assertions from the copy if the agent already
   added them, so the only order-result assertion is the confirmation message.
   Select **Sauce Labs Backpack** and run:

   ```bash
   uv run pytest lab04/test_checkout_demo.py -v
   ```

   Expected: **1 passed**. The Backpack checkout reaches confirmation.
3. Change only the add-to-cart action to **Sauce Labs Bike Light**. If using an
   ID locator, change `add-to-cart-sauce-labs-backpack` to
   `add-to-cart-sauce-labs-bike-light`. If using a product row or text locator,
   change the selected row instead. Keep the requirement as Backpack. Run:

   ```bash
   uv run pytest lab04/test_checkout_demo.py -v
   ```

   Expected: **1 passed again**. The confirmation message appears for either
   product. That assertion alone cannot catch the wrong order.

## Presenter demo: check Overview before Finish

In the temporary copy, add checks **after Overview is visible and before clicking
Finish**. Use the generated test's wait variable, or create one as below. These
locators should be checked against the page you observed in Lab 3:

```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Insert here after Continue opens Overview, before the Finish click.
wait = WebDriverWait(driver, 10)
wait.until(EC.url_to_be("https://www.saucedemo.com/checkout-step-two.html"))
items = wait.until(EC.visibility_of_all_elements_located(
    (By.CSS_SELECTOR, '[data-test="inventory-item"]')
))
assert len(items) == 1, f"Expected one cart row, got {len(items)}"
item = items[0]
name = item.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]').text
quantity = item.find_element(By.CSS_SELECTOR, '[data-test="item-quantity"]').text
assert name == "Sauce Labs Backpack", f"Wrong product: {name}"
assert quantity == "1", f"Expected quantity 1, got {quantity}"
# Keep the existing Finish action and final confirmation assertion below.
```

One row alone is not enough: check the product name and its quantity too.

1. Keep the add-to-cart action set to Bike Light and run:

   ```bash
   uv run pytest lab04/test_checkout_demo.py -v
   ```

   Expected: **1 failed**, at the product-name assertion. Pytest should show
   `Wrong product: Sauce Labs Bike Light` and the actual Bike Light name versus
   the expected Backpack. A timeout or missing element is not this result.
2. Restore the add-to-cart action to Backpack, keeping the new assertions, and
   run the same command. Expected: **1 passed**.
3. Remove the temporary copy after the demo so it cannot be collected later:

   ```bash
   rm lab04/test_checkout_demo.py
   ```

## Student practice

1. Open your original `lab03/test_checkout.py`. Find the assertion that checks
   the product in the order. Does it also check exactly one Backpack?
2. If missing, add Overview assertions before Finish. If already present,
   use the wrong-product run below to verify them. Keep the final confirmation
   assertion as well.
3. Change **only the product added to the cart** to Bike Light. Keep the expected
   product name as **Sauce Labs Backpack** and expected quantity as **1**. Do not
   derive the expected product from the selected item or change both together.
4. Run:

   ```bash
   uv run pytest lab03/test_checkout.py -v
   ```

   Expected: **1 failed because the actual product is Bike Light**, at the
   product assertion on Overview. Inspect the failure to verify the cause.
5. Restore the add-to-cart action to Backpack. Keep the reviewed assertions and
   rerun the same command. Expected: **1 passed**.

## Result check

| Assertions | Added product | Expected result |
| --- | --- | --- |
| Confirmation only | Backpack | Pass |
| Confirmation only | Bike Light | Pass, exposing a gap |
| Overview: one Backpack with quantity 1, plus confirmation | Bike Light | Fail because of the product name |
| Overview: one Backpack with quantity 1, plus confirmation | Backpack | Pass |

Submit the reviewed **`lab03/test_checkout.py`** with Backpack restored as part of
the whole tutorial ZIP. Follow [Submission](../README.md#submission) for the file
name and archive contents.
