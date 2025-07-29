import pytest
from pages.home_page import HomePage


# 15
def test_logo_is_visible(page):
    home_page = HomePage(page)
    home_page.go_to()

    assert home_page.logo_image.is_visible()


# 16
def test_register_button_is_visible(page):
    home_page = HomePage(page)
    home_page.go_to()
    register_button = page.get_by_role("button", name="Register")
    assert register_button.is_visible()


# 17
def test_login_button_is_visible(page):
    home_page = HomePage(page)
    home_page.go_to()
    login_button = page.get_by_role("button", name="Login")
    assert login_button.is_visible()


# 18
def test_winna_originals_carousel_buttons(page):
    home_page = HomePage(page)
    home_page.go_to()

    # Scroll right 2 times
    for _ in range(2):
        home_page.button_winna_original_right.click()

    # Check if right button is visually disabled
    right_class = home_page.button_winna_original_right.get_attribute("class")
    assert "text-body-level-3" in right_class

    # Scroll left 2 times
    for _ in range(2):
        home_page.button_winna_original_left.click()

    # Check if left button is visually disabled
    left_class = home_page.button_winna_original_left.get_attribute("class")
    assert "text-body-level-3" in left_class


# 18
def test_providers_carousel_navigation(page):
    home_page = HomePage(page)
    home_page.go_to()

    for _ in range(2):
        home_page.button_providers_right.click()

    page.wait_for_timeout(500)

    right_class = home_page.button_providers_right.get_attribute("class")
    assert "text-body-level-3" in right_class  # or any other gray/disabled class

    for _ in range(2):
        home_page.button_providers_left.click()

    page.wait_for_timeout(500)
    left_class = home_page.button_providers_left.get_attribute("class")
    assert "text-body-level-3" in left_class


# 18
def test_slots_carousel_navigation(page):
    home_page = HomePage(page)
    home_page.go_to()

    for _ in range(2):
        home_page.button_slots_right.click()

    # Check if right button becomes visually disabled (via class)
    right_button_class = home_page.button_slots_right.get_attribute("class")
    assert "disabled:text-body-level-3" in right_button_class

    for _ in range(2):
        home_page.button_slots_left.click()

    left_button_class = home_page.button_slots_left.get_attribute("class")
    assert "disabled:text-body-level-3" in left_button_class


# 18
def test_game_shows_carousel_navigation(page):
    home_page = HomePage(page)
    home_page.go_to()

    for _ in range(2):
        home_page.button_game_shows_right.click()

    right_button_class = home_page.button_game_shows_right.get_attribute("class")
    assert "disabled:text-body-level-3" in right_button_class

    for _ in range(2):
        home_page.button_game_shows_left.click()

        # Assert the left button has the disabled class
    left_button_class = home_page.button_game_shows_left.get_attribute("class")
    assert "disabled:text-body-level-3" in left_button_class
