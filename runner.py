__author__ = 'ldemacex'

import os
import sys
from behave import __main__ as runner
from utils.argument_parser import ArgumentParserContext
from springpython.context import ApplicationContext


def init_context():
    return ApplicationContext(ArgumentParserContext())


def set_environment_data(spring_context):
    parser = spring_context.get_object("ArgumentParser")
    parser.set_up_environment_variables()
    parser.recovery_behave_args()


if __name__ == "__main__":
    set_environment_data(init_context())
    runner.main()


