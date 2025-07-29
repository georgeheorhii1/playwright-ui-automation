from playwright.sync_api import sync_playwright

import json
import os
import pytest


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def test_data():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "test_data.json"))
    with open(file_path) as f:
        return json.load(f)
