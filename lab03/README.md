# Lab 3: Agentic checkout

## Goal and setup

Use a coding agent to explore <https://www.saucedemo.com/> and write one checkout
test. Open **this repository root** in an agent that can edit files, run terminal
commands and access the site in a browser. Install Google Chrome and run from
the repository root:

```bash
uv sync
uv run pytest lab02/test_login.py::test_login_success -v
```

The second command checks the browser setup. The agent must reuse the `driver`
fixture in `conftest.py`, which creates and closes a fresh Chrome session for
each test. Visible Chrome is the default. For an environment without a display,
the agent can add `--headless` to pytest; Chrome and network access are still
required. If browser exploration is unavailable, use an agent environment that
provides it and report any blocked step accurately.

The file to create is **`lab03/test_checkout.py`**. It is intentionally absent in
the starter. Keep agent edits scoped to that file.

## Checkout requirement

Order **exactly one Sauce Labs Backpack** with the public demo account. Checkout
goes through **Cart**, the **Your Information** form, **Overview**, and the order
confirmation screen. Use fictional first name, last name and postal code, such
as `Alex`, `Taylor`, `2000`. Complete the demo checkout until confirmation appears.

## Presenter demo

1. Show the repository root, `conftest.py` and the checkout requirement.
2. Run the exact prompt below in the coding agent before students try it.
3. Watch the agent explore the browser, create the test, run pytest and report
   its actual result. If execution is blocked, show the observed error.
4. Open the resulting `lab03/test_checkout.py`. Identify its locators, waits,
   actions and assertions. Keep it for the review in Lab 4.

## Copy this prompt

```text
Act as a browser testing agent. Explore https://www.saucedemo.com/
in a browser and test its end-to-end checkout flow.

Use the public demo account standard_user / secret_sauce. The shopper
wants to order exactly one Sauce Labs Backpack. Use fictional customer
details and complete checkout until the order confirmation appears.

Discover the interactions and locators through browser observation.
Write one Python end-to-end test using Selenium and pytest. Reuse the
driver fixture provided by the repository. Save the test to
lab03/test_checkout.py and keep your edits scoped to that file.

Run:
uv run pytest lab03/test_checkout.py -v

If execution fails, inspect the browser or pytest output and decide
what to check next. Keep the expected behavior tied to the requirement.
Report the file you created and the actual pytest result. If the
environment blocks execution, identify the step and the observed error.
```

## Student practice and result check

Run the same prompt on **your own copy of the repository**. Open the generated
file and explain what each part does. Confirm that the test reuses `driver`,
logs in, adds the item, visits Cart, fills Your Information, visits Overview and
finishes the order. Read what the assertions actually check.

From the repository root, rerun the generated test yourself:

```bash
uv run pytest lab03/test_checkout.py -v
```

Expected after the agent completes the task: **1 passed**, with the confirmation
`Thank you for your order!` visible at the end. Record the actual pytest result;
do not claim a pass if Chrome or site access failed. For headless execution:

```bash
uv run pytest lab03/test_checkout.py -v --headless
```

A passing test is the starting point for [Lab 4](../lab04/README.md), where you
will check whether the assertions enforce the requested product and quantity.
