import pytest
from pages.login_interface import LoginPage


def test_login_tab_is_selected_by_default(page):
    page.goto("https://shuffle.com/", wait_until="domcontentloaded", timeout=20000)

    page.get_by_role("button", name="Login").click()

    login_page = LoginPage(page)

    class_attr = login_page.login_tab.get_attribute("class")
    print("🔍 class attribute:", class_attr)
    assert "active" in class_attr


def test_login_button_disabled_if_only_email_filled(page):
    page.goto("https://shuffle.com/", wait_until="domcontentloaded", timeout=20000)
    page.get_by_role("button", name="Login").click()

    login_page = LoginPage(page)
    login_page.email_input.fill("george@example.com")

    assert not login_page.login_button.is_enabled()


def test_login_button_disabled_if_only_password_filled(page):
    page.goto("https://shuffle.com/", wait_until="domcontentloaded", timeout=20000)
    page.get_by_role("button", name="Login").click()

    login_page = LoginPage(page)
    login_page.password_input.fill("Degault_pass")

    assert not login_page.login_button.is_enabled()


def test_forgot_password_link_is_visible_and_clickable(page):
    page.goto("https://shuffle.com/", wait_until="domcontentloaded", timeout=20000)
    page.get_by_role("button", name="Login").click()

    login_page = LoginPage(page)

    login_page.email_input.wait_for(timeout=5000)

    assert login_page.forgot_password_link.is_visible()
    assert login_page.forgot_password_link.is_enabled()
