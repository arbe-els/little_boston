import pytest
from playwright.sync_api import sync_playwright
from pages.page_start import StartPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture
def start_page(page) -> StartPage:
    start = StartPage(page)
    return start

@pytest.fixture
def login_user(start_page):
    def _login(username: str, password: str = "secret_sauce"):
        start_page.open_website()
        start_page.enter_username(username)
        start_page.enter_password(password)
        start_page.click_login()
        return start_page
    return _login