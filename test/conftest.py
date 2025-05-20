import pytest
from selene import browser

@pytest.fixture(scope='function', autouse=True)

def browser_settings():
    browser.config.type_by_js=True
    # browser.config.click_by_js=True
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'

    yield

    browser.quit()