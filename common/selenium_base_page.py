__author__ = 'Leonardo De Macedo'


from selenium.webdriver import Firefox

class BasePage(Firefox):

    WEB_DRIVER_TIMEOUT = 15

    def __init__(self, web_driver):
        self.driver = web_driver.driver()
        self.driver.implicitly_wait(self.WEB_DRIVER_TIMEOUT)

    def open_url(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.driver.quit()

