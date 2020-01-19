import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="firefox",
                     help="Choose browser: chrome or firefox (other browsers aren't supported)")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: es, en, ru (default), de, etc.")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print("Browser {} still is not implemented or his name is not correct".format(browser_name))
        raise Exception()
    yield browser
    browser.quit()