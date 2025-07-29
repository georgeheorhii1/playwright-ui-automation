from pages.base_page import BasePage


class LoginModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.email_input = page.get_by_placeholder("Enter username")
        self.password_input = page.get_by_placeholder("Enter password")
        self.login_button = page.get_by_role("dialog").get_by_role("button", name="Login")


class VerificationModal(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.verify_button = page.get_by_role("button", name="Verify")
