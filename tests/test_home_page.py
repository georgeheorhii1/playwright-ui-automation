import pytest
from pages.home_page import HomePage


def test_logo_is_visible_and_clickable(page):
    home_page = HomePage(page)
    home_page.go_to()

    assert home_page.logo_link.is_visible()

    home_page.logo_link.click()
    page.wait_for_url("https://shuffle.com/")
    assert page.url == "https://shuffle.com/"


def test_register_button_is_visible(page):
    page.goto("https://shuffle.com/")
    register_button = page.get_by_role("button", name="Register")
    assert register_button.is_visible()


def test_login_button_is_visible(page):
    page.goto("https://shuffle.com/")
    login_button = page.get_by_role("button", name="Login")
    assert login_button.is_visible()
