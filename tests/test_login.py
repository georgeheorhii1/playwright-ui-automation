import pytest
from utils import load_test_data

test_data = load_test_data()
from pages.modals import LoginModal, VerificationModal


def test_login_with_invalid_password(page):
    page.goto("https://shuffle.com/", wait_until="domcontentloaded", timeout=60000)
    page.get_by_role("button", name="Login").click()
    login_modal = LoginModal(page)
    email = test_data["invalid_login"]["email"]
    password = test_data["invalid_login"]["password"]
    login_modal.email_input.fill(email)
    login_modal.password_input.fill(password)
    login_modal.login_button.click()
    assert page.get_by_role("button", name="Verify").is_hidden()


def test_login_process_negative(page):
    page.goto("https://shuffle.com/", wait_until="domcontentloaded", timeout=60000)
    login_button = page.get_by_role("button", name="Login")
    login_button.click()
    page.get_by_placeholder("Enter Email or Username").wait_for()
    login_modal = LoginModal(page)
    email = test_data["valid_login"]["email"]
    password = test_data["valid_login"]["password"]
    login_modal.email_input.fill(email)
    login_modal.password_input.fill(password)
    verification_modal = VerificationModal(page)
    login_modal.login_button.click()
    input("🔐 Please enter the 2FA code in the browser, then press Enter to continue...")
    verification_modal.verify_button.click()
    print("✅ Login test completed successfully.")
    page.context.close()


def test_login_button_disabled_until_fields_filled(page):
    page.goto("https://shuffle.com/", wait_until="domcontentloaded", timeout=60000)
    login_button = page.get_by_role("button", name="Login")
    login_button.click()
    login_modal = LoginModal(page)

    assert not login_modal.login_button.is_enabled()

    email = test_data["invalid_login"]["email"]
    password = test_data["valid_login"]["password"]

    # First: only password filled
    login_modal.email_input.fill("")
    login_modal.password_input.fill(password)
    assert not login_modal.login_button.is_enabled()

    # Second: only email filled
    login_modal.email_input.fill(email)
    login_modal.password_input.fill("")
    assert not login_modal.login_button.is_enabled()

    print("Login test (negative) is completed successfully.")
    page.context.close()
