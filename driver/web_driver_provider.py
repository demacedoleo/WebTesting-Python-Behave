__author__ = 'ldemacex'

from firefox_web_driver_provider import FireFoxWebDriver


class WebDriverProvider(object):

    def __init__(self, browser="Chrome"):
        self.driver = self.get_web_driver(browser)

    def get_web_driver(self, browser):
        driver = None
        if browser.lower() == "firefox":
            driver = FireFoxWebDriver().driver

        return driver




