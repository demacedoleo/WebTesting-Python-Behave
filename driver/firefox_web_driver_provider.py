__author__ = 'ldemacex'

from selenium import webdriver


class FireFoxWebDriver(object):

    def __init__(self):
        self.driver = self.get_web_driver()

    def get_web_driver(self):
        return webdriver.Firefox
