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
