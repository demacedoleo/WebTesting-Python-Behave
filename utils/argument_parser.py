__author__ = 'ldemacex'

import sys
import argparse


class ArgumentParser(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-b',
                            '--browser',
                            default="firefox",
                            choices=['firefox', 'chrome', 'ie', 'phantomjs'],
                            dest="browser",
                            help='firefox, \
                            chrome, \
                            ie (internet_explorer, \
                            only available in selenium grid),\
                            phantomjs (Default: firefox). \
                            No aditional actions are required to use \
                            this argument, if needed this is accessible from \
                            the testing solution using the "BROWSER" \
                            environment variable',
                            required=False)
        self.parser.parse_args(sys.argv[1:])
        pass

    def get_argument(self):
        return self.parser.parse_args().browser
