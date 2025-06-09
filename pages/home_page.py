class HomePage:
    def __init__(self, page):
        self.page = page
        self.logo_link = page.get_by_role("link", name="Home").first

    def go_to(self):
        self.page.goto("https://shuffle.com/")

