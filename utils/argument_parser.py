__author__ = 'Leonardo De Macedo'

import os
import sys
import argparse
from springpython.config import PythonConfig
from springpython.config import Object


class ArgumentParser(object):
    """
    Class in charge of parse arguments and re build behave tags
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-b', '--browser', default="chrome", dest="browser", help='browser', required=False)
        self.parser.add_argument('-u', '--url', default="host", dest="host", help='host', required=False)
        self.parser.add_argument('-p', '--port', default="port", dest="port", help='port', required=False)
        self.parser.add_argument('-e', '--env', default="env", dest="env", help='env', required=False)
        self.parser.add_argument('-t', '--tags', action="append", dest="tags", help='tags', required=False)
        self.parser.parse_args(sys.argv[1:])

    def set_up_environment_variables(self):
        """
        Used to set variables and define the environment
        """
        args = vars(self.parser.parse_args())
        for key, value in args.iteritems():
            if key != "tags":
                os.environ[key] = value

    def recovery_behave_args(self):
        """
        Used to set tags according the behave framework
        """
        tags = vars(self.parser.parse_args())
        del sys.argv[1:]

        if tags['tags'] is not None:
            for tag in tags['tags']:
                sys.argv.append('--tags')
                sys.argv.append(tag)
                if tag.upper() in ["WIP", "@WIP"]:
                    run_wip_tests = True


class ArgumentParserContext(PythonConfig):
    """
    Used to set the ArgumentParser into spring container
    """

    def __init__(self):
        super(ArgumentParserContext, self).__init__()

    @Object(lazy_init=True)
    def ArgumentParser(self):
        parser = ArgumentParser()
        return parser
