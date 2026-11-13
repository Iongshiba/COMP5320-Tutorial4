"""Shared Chrome fixture for the browser labs."""

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run Chrome without a visible window (default: visible Chrome).",
    )


@pytest.fixture(scope="function")
def driver(request):
    """Give each test a fresh Chrome session and always close it afterwards."""
    options = webdriver.ChromeOptions()
    if request.config.getoption("--headless"):
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1280,900")
    # Keep password-manager popups out of the classroom demo.
    options.add_experimental_option(
        "prefs",
        {"credentials_enable_service": False, "profile.password_manager_enabled": False},
    )

    browser = webdriver.Chrome(options=options)
    try:
        browser.set_page_load_timeout(30)
        yield browser
    finally:
        browser.quit()
