__author__ = 'ldemacex'

from springpython.config import XMLConfig
from springpython.context import ApplicationContext


BEHAVE_DEBUG_ON_ERROR = True

def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


def before_all(context):
    configuration = XMLConfig("resources/spring/application-context.xml")
    context.spring = ApplicationContext(configuration)
    context.browser = context.spring.get_object("ArgParser").parser.parse_args().browser
