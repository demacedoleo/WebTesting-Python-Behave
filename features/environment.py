__author__ = 'ldemacex'

import os
from springpython.config import XMLConfig
from springpython.context import ApplicationContext


BEHAVE_DEBUG_ON_ERROR = True


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    configuration = XMLConfig("resources/spring/application-context.xml")
    context.spring = ApplicationContext(configuration)
    context.browser = os.environ['browser']


def before_scenario(context, scenario):
    context.driver = None


def after_scenario(context, scenario):
    scenario
    quit_web_driver(context)


def quit_web_driver(context):
    if context.driver is not None:
        pass
