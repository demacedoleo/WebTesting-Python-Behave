__author__ = 'ldemacex'

from behave import Given, When, Then
from driver.web_driver_provider import WebDriverProvider
from pages.landing_page_po import LandingPageImpl
from selenium import webdriver

@Given(u'A googler open the "{url}"')
def step_impl(context, url):
    context.landing_page = context.spring.get_object("LandingPageImpl")
    context.landing_page.open_url(url)


@When(u'Search to get information about "{key_word}"')
def step_impl(context, key_word):
    pass


@Then(u'Verify that web page contains at least "{amount:d}" links')
def step_impl(context, amount):
    pass



