class LoginModal:
    def __init__(self, page):
        self.page = page
        self.email_input = page.get_by_placeholder("Enter Email or Username")
        self.password_input = page.get_by_placeholder("Enter Password")
        self.login_button = page.locator("form#login-form").get_by_role("button", name="Login")


class VerificationModal:
    def __init__(self, page):
        self.page = page
        self.verify_button = page.get_by_role("button", name="Verify")
