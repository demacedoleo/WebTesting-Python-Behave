__author__ = 'ldemacex'


from selenium.webdriver.common.by import By
from common.selenium_base_page import BasePage


class LandingPageImpl(BasePage):
    """
    Page Object in charge of interact with google search
    """

    INPUT_SEARCH = (By.XPATH, "//input[@name='q']")

    def launch_browser(self, url):
        self.open_url(url)

    def do_search(self, text):
        self.find_element_by_xpath(self.INPUT_SEARCH).clear()
        self.find_element_by_xpath(self.INPUT_SEARCH).send_keys(text)
