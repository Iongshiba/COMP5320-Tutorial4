"""Selenium login practice. Run all commands from the repository root."""

import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_login_success(driver):
    """WORKED EXAMPLE: a standard user reaches the Products page."""
    # Arrange
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    time.sleep(2)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    time.sleep(2)
    # Act
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # Assert
    title = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]')
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
