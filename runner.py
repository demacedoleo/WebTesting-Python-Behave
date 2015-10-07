__author__ = 'ldemacex'

import sys
from behave import __main__ as runner

from springpython.config import XMLConfig
from springpython.context import ApplicationContext

def blah():
    print 'Hola'


if __name__ == "__main__":
    ApplicationContext(XMLConfig("resources/spring/application-context.xml"))
    del sys.argv[1:]
    runner.main()


