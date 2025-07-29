import pytest

from pages.home_page import HomePage
from pages.modals import LoginModal


# 11
def test_login_modal_opens_correctly(page):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    login_modal.email_input.wait_for(timeout=5000)

    assert login_modal.password_input.is_visible()
    assert login_modal.login_button.is_visible()
    assert not login_modal.login_button.is_enabled()  # Disabled if fields are empty


# 12
def test_login_button_disabled_if_only_email_filled(page, test_data):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    email = test_data["invalid_login"]["email"]

    login_modal.email_input.fill(email)

    assert not login_modal.login_button.is_enabled()


# 13
def test_login_button_disabled_if_only_password_filled(page, test_data):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    password = test_data["invalid_login"]["password"]

    login_modal.password_input.fill(password)

    assert not login_modal.login_button.is_enabled()


# 14
def test_forgot_password_link_is_visible_and_clickable(page):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    login_modal.email_input.wait_for(timeout=5000)

    assert login_modal.forgot_password_link.is_visible()
    assert login_modal.forgot_password_link.is_enabled()

