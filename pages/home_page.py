from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.logo_image = page.locator("header img[alt='Logo']").first
        self.button_winna_original_right = page.locator(
            "section:has-text('Winna Originals') button[data-direction='1']")
        self.button_winna_original_left = page.locator(
            "section:has-text('Winna Originals') button[data-direction='-1']")
        self.button_providers_right = page.locator("section:has-text('Providers') button[data-direction='1']")
        self.button_providers_left = page.locator("section:has-text('Providers') button[data-direction='-1']")
        self.button_slots_left = page.locator("section:has-text('Slots') button[data-direction='-1']")
        self.button_slots_right = page.locator("section:has-text('Slots') button[data-direction='1']")
        self.button_game_shows_left = page.locator("section:has-text('Game Shows') button[data-direction='-1']")
        self.button_game_shows_right = page.locator("section:has-text('Game Shows') button[data-direction='1']")
        self.button_profile = page.locator('button[data-profile="true"]')
        self.button_logout = page.get_by_role("button", name="Log Out")

    def go_to(self):
        self.page.goto("https://webapp-2ldl.onrender.com/")
