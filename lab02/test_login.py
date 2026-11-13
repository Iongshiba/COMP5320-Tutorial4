"""Selenium login practice. Run all commands from the repository root."""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login_success(driver):
    """WORKED EXAMPLE: a standard user reaches the Products page."""
    # Arrange
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys(
        "standard_user"
    )
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # Act
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()

    # Assert: wait for the visible result, then check the page and its title.
    wait.until(EC.url_to_be("https://www.saucedemo.com/inventory.html"))
    title = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="title"]'))
    )
    assert title.text == "Products"


def test_login_wrong_password(driver):
    """TODO: standard_user + a wrong password stays at login with a credentials error."""
    # Open the login page, submit the credentials, wait for the error,
    # and assert both the error message and the visible login form.
    pytest.fail("TODO: implement this test")


def test_login_locked_user(driver):
    """TODO: locked_out_user + secret_sauce stays at login with a locked-user error."""
    # Use a fresh login, wait for the error, then check its message and the login form.
    pytest.fail("TODO: implement this test")
