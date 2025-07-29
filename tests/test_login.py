import pytest
from pages.modals import LoginModal, VerificationModal
from pages.home_page import HomePage


# TC_7/1
def test_login_with_invalid_data_throttling(page, test_data):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    email = test_data["invalid_login"]["email"]
    password = test_data["invalid_login"]["password"]

    for i in range(10):
        login_modal.email_input.fill(email)
        login_modal.password_input.fill(password)
        login_modal.login_button.click()
        page.wait_for_timeout(500)

    assert home.is_hidden("text=Please enter the code from your authenticator app.")


# TC_7/2
def test_login_with_invalid_password(page, test_data):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    email = test_data["invalid_login"]["email"]
    password = test_data["invalid_login"]["password"]

    login_modal.email_input.fill(email)
    login_modal.password_input.fill(password)
    login_modal.login_button.click()

    assert home.is_hidden("text=Please enter the code from your authenticator app.")


# passed TC_1
def test_login_process_positive_without_2fa(page, test_data):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    email = test_data["valid_login"]["email"]
    password = test_data["valid_login"]["password"]

    login_modal.email_input.fill(email)
    login_modal.password_input.fill(password)
    login_modal.login_button.click()

    page.wait_for_timeout(2000)

    assert home.get_by_role("text", "Wallet").is_visible()


# TC_8
def test_login_button_disabled_until_fields_filled(page, test_data):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)

    # Nothing filled
    class_attr = login_modal.login_button.get_attribute("class")
    assert "opacity-50" in class_attr

    email = test_data["invalid_login"]["email"]
    password = test_data["valid_login"]["password"]

    # Only password filled
    login_modal.email_input.fill("")
    login_modal.password_input.fill(password)
    class_attr = login_modal.login_button.get_attribute("class")
    assert "opacity-50" in class_attr

    # Only email filled
    login_modal.email_input.fill(email)
    login_modal.password_input.fill("")
    class_attr = login_modal.login_button.get_attribute("class")
    assert "opacity-50" in class_attr


# TC_19
def test_login_and_logout_case(page, test_data):
    home = HomePage(page)
    home.goto()
    home.click_by_role("button", "Login")

    login_modal = LoginModal(page)
    email = test_data["valid_login"]["email"]
    password = test_data["valid_login"]["password"]

    login_modal.email_input.fill(email)
    login_modal.password_input.fill(password)
    login_modal.login_button.click()

    page.wait_for_timeout(2000)

    assert home.get_by_text("Wallet").is_visible()

    home.button_profile.click()
    home.button_logout.click()

    assert home.get_by_text("Sign up").is_visible()
