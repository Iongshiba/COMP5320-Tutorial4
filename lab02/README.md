# Lab 2: Selenium login with pytest

## Goal and setup

Test visible login results on <https://www.saucedemo.com/> using Selenium 4 and
pytest. Install Google Chrome, check that the site opens, and run from the
repository root:

```bash
uv sync
```

Read the shared `driver` fixture in `conftest.py`. It starts a fresh visible
Chrome session for each test and closes it after the test. Selenium Manager may
need network access to download ChromeDriver on the first run.

File to edit: **`lab02/test_login.py`**. Keep the complete demo test and fill in
the two TODO functions. Remove `pytest.fail("TODO: implement this test")` when
you implement each test.

## Presenter demo

1. Open `test_login_success(driver)` and explain AAA. The fixture supplies
   Chrome; the test uses ID locators for the username, password and Login button.
2. Run the worked example:

   ```bash
   uv run pytest lab02/test_login.py::test_login_success -v
   ```

3. Watch it type `standard_user` / `secret_sauce` and click **Login**. Explain
   the explicit waits for the inventory URL and the visible **Products** title.
   Expected result: **1 passed**, with the Products page shown before Chrome closes.
   The window closes automatically, so open the code alongside the run.

The example uses `WebDriverWait` and `expected_conditions` to wait for a UI
result. Use the same approach in your tests instead of fixed sleeps. See the
[Selenium waits guide](https://www.selenium.dev/documentation/webdriver/waits/).

## Student practice

| Function | Credentials | Expected UI result |
| --- | --- | --- |
| `test_login_wrong_password(driver)` | `standard_user` / `wrong_password` | Stay on login; show a credentials error |
| `test_login_locked_user(driver)` | `locked_out_user` / `secret_sauce` | Stay on login; show a locked-user error |

For each TODO:

1. Open the login page and enter the specified credentials.
2. Click **Login** and explicitly wait for the visible error element
   (`[data-test="error"]`).
3. Assert the relevant error text. Wrong password:
   `Epic sadface: Username and password do not match any user in this service`.
   Locked user: `Epic sadface: Sorry, this user has been locked out.`
4. Also assert that the login form is still visible and the URL remains
   `https://www.saucedemo.com/`. Checking only that Products is absent is too weak.

Before implementation, these functions intentionally fail with
`TODO: implement this test` once Chrome starts successfully. They are exercises,
not skipped or passing tests.

## Check your result

After completing both TODOs, run the whole file:

```bash
uv run pytest lab02/test_login.py -v
```

Expected after completion: **3 passed**. Each case has a separate Chrome session.
If an assertion fails, inspect the actual page and pytest output before changing
anything. Keep the intended behavior as the expectation.

For an agent or a machine without a display, add `--headless`:

```bash
uv run pytest lab02/test_login.py::test_login_success -v --headless
uv run pytest lab02/test_login.py -v --headless
```

Headless mode still needs Chrome, a matching driver and access to the site. If
setup or navigation is blocked, record the step and the actual error, then retry
the visible demo command on the presenter's machine.
