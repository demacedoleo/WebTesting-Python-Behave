__author__ = 'Leonardo De Macedo'


from behave import Given, When, Then


@Given(u'A googler open the "{url}"')
def step_impl(context, url):
    context.pages = dict()
    context.pages["landing_page"] = context.container.get_object("LandingPageImpl")
    context.pages["landing_page"].open_url("http://www.google.com")


@When(u'Search to get information about "{key_word}"')
def step_impl(context, key_word):
    context.pages["landing_page"].do_search(key_word)


@Then(u'Verify that web page contains at least "{amount:d}" links')
def step_impl(context, amount):
    actual_links = context.pages["landing_page"].get_links_amount()
    assert amount <= actual_links, "Expected <= %s - Actual: %s" % (amount, actual_links)
    context.pages["landing_page"].driver.quit()



