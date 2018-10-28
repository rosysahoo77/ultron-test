import pytest
from selenium.webdriver import firefox,chrome,ie

def get_driver_instance():
    browser = pytest.config.option.browser.lower()
    url = pytest.config.option.server.lower()

    if browser == 'firefox':
        driver = firefox("./browser-servers/geckodriver.exe")
    elif browser == 'chrome':
        driver = chrome("./browser-servers/chromedriver.exe")
    elif browser == 'ie':
        driver = chrome("./browser-servers/internetexplorer.exe")
    else:
        print('invalid browser option')
        return None
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url== 'prod':
        driver.get('https://demo.actitime.com')
    else:
        driver.get("https:localhost")
    return driver
