class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click_by_role(self, role, name):
        self.page.get_by_role(role, name=name).click()

    def get_by_role(self, role, name):
        return self.page.get_by_role(role, name=name)

    def get_by_placeholder(self, placeholder):
        return self.page.get_by_placeholder(placeholder)

    def wait_for_selector(self, selector, timeout=5000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def is_hidden(self, selector):
        return self.page.locator(selector).is_hidden()
