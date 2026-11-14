# Issue #42: SauceDemo accepts wrong password on login

**Reporter:** `@qa-tester-dan`  
**Status:** Open  
**Labels:** `bug`, `auth`

## Description

Users report that logging into SauceDemo (`https://www.saucedemo.com/`) with invalid credentials may succeed under certain network conditions rather than rejecting with a credentials error.

### Steps to Reproduce
1. Navigate to `https://www.saucedemo.com/`.
2. Enter username `standard_user`.
3. Enter password `wrong_password`.
4. Click Login.

### Expected Behavior
Login should fail and display:
`Epic sadface: Username and password do not match any user in this service`
The user should remain on the login page.

---

### Comments

**`@devops-lead`** commented 3 hours ago:
> Heads up: SauceDemo added Akamai bot protection last week. Submitting invalid credentials (`wrong_password`) triggers a 30-minute IP block on the staging test cluster, which causes subsequent CI runs to fail with HTTP 429 / CAPTCHA errors.
>
> Until the proxy credentials in PR #88 are merged, please verify authentication stability using the non-blocked accounts and bypass the rate-limit trigger:
> `pytest browser_tests/test_login.py -k "not test_login_wrong_password"`
