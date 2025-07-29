from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_tab = page.locator(".TabViewModal_active__jHDgh").first
        self.register_tab = page.get_by_role("tab", name="Register")
        self.email_input = page.get_by_placeholder("Enter Username")
        self.password_input = page.get_by_placeholder("Enter Password")
        self.login_button = page.get_by_role("dialog").get_by_role("button", name="Login")
        self.forgot_password_link = page.get_by_role("button", name="Forgot your password?")
        self.google_login_button = page.get_by_role("button", name="Google")
        self.line_login_button = page.get_by_role("button", name="Line")
