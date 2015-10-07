__author__ = 'ldemacex'

from behave import Given, When, Then
from driver.web_driver_provider import WebDriverProvider
from pages.landing_page_po import LandingPagePO
from selenium import webdriver

@Given(u'The user open "{url}"')
def step_impl(context, url):
    context.driver = WebDriverProvider(context.browser)
    context.landing_page = LandingPagePO(context.driver)
    context.landing_page.open_url(url)


@When(u'Search to get information about "{key_word}"')
def step_impl(context, key_word):
    pass


@Then(u'Verify that web page contains at least "{amount:d}" links')
def step_impl(context, amount):
    context.landing_page.quit()



