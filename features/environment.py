__author__ = 'Leonardo De Macedo'


from springpython.config import XMLConfig
from springpython.context import ApplicationContext


def before_all(context):
    configuration = XMLConfig("resources/spring/application-context.xml")
    context.container = ApplicationContext(configuration)


def before_scenario(context, scenario):
    context.driver = None
    

def after_scenario(context, scenario):
    quit_web_driver(context)


def quit_web_driver(context):
    if context.driver is not None:
        pass