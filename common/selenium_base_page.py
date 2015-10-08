__author__ = 'ldemacex'


class BasePage(object):

    def __init__(self, web_driver):
        self.driver = web_driver.driver()

    def open_url(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.driver.quit()

