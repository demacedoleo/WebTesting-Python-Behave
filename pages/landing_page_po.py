__author__ = 'Leonardo De Macedo'


from selenium.webdriver.common.by import By
from common.selenium_base_page import BasePage


class LandingPageImpl(BasePage):
    """
    Page Object in charge of interact with google search
    """

    INPUT_SEARCH = (By.XPATH, '//input[@id="lst-ib"]')
    BUTTON_SEARCH = (By.XPATH, '//button[@class="lsb"]')
    LINKS_SEARCH = (By.XPATH, '//h3[@class="r"]/a')

    def __init__(self, web_driver):
        super(LandingPageImpl, self).__init__(web_driver)

    def launch_browser(self, url):
        """
        Open url
        :param url:
        """
        self.open_url(url)

    def do_search(self, text):
        """
        Make  google searchs
        :param text:
        """
        self.driver.find_element(*self.INPUT_SEARCH).clear()
        self.driver.find_element(*self.INPUT_SEARCH).send_keys(text)
        self.driver.find_element(*self.BUTTON_SEARCH).click()

    def verify_links(self, key_word):
        """
        Verify that links contains some keyword
        :param key_word:
        :return: Boolean
        """
        contains_key_word = True
        web_elements = self.driver.find_elements(*self.LINKS_SEARCH)
        for link in web_elements:
            if key_word not in link.get_text():
                contains_key_word = False
                break
        return contains_key_word

    def get_links_amount(self):
        """
        Obtain amount of link by search
        :return: links amount
        """
        return len(self.driver.find_elements(*self.LINKS_SEARCH))



