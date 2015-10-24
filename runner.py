__author__ = 'Leonardo De Macedo'


from behave.configuration import Configuration, ConfigError
from behave.runner import Runner, Context
from springpython.context import ApplicationContext
from utils.argument_parser import ArgumentParserContext


def init_context():
    """
    Initialize spring context in order to parse arguments
    """
    return ApplicationContext(ArgumentParserContext())


def set_environment_data(spring_context):
    """
    Parser Arguments & Set variables into environment
    """
    parser = spring_context.get_object("ArgumentParser")
    parser.set_up_environment_variables()
    parser.recovery_behave_args()


class CustomBehave(Runner):
    """
    Class in charge of run scenarios using multi thread
    """

    def __init__(self, args=None):
        config = Configuration(args)
        super(CustomBehave, self).__init__(config)
        self.config.format = ['pretty']

    def run_model(self, features=None):
        """
        Re write run_model to run tests in multi threads
        :param features:
        :return:
        """
        if not self.context:
            self.context = Context(self)
        if features is None:
            features = self.features

        # -- ENSURE: context.execute_steps() works in weird cases (hooks, ...)
        context = self.context
        self.setup_capture()
        self.run_hook('before_all', context)

        run_feature = not self.aborted
        failed_count = 0
        undefined_steps_initial_size = len(self.undefined_steps)
        for feature in features:
            if run_feature:
                try:
                    self.feature = feature
                    for formatter in self.formatters:
                        formatter.uri(feature.filename)
                    #TODO: Implement multithread here
                    failed = feature.run(self)
                    if failed:
                        failed_count += 1
                        if self.config.stop or self.aborted:
                            # -- FAIL-EARLY: After first failure.
                            run_feature = False
                except KeyboardInterrupt:
                    self.aborted = True
                    failed_count += 1
                    run_feature = False

            # -- ALWAYS: Report run/not-run feature to reporters.
            # REQUIRED-FOR: Summary to keep track of untested features.
            for reporter in self.config.reporters:
                reporter.feature(feature)

        # -- AFTER-ALL:
        if self.aborted:
            print("\nABORTED: By user.")
        for formatter in self.formatters:
            formatter.close()
        self.run_hook('after_all', self.context)
        for reporter in self.config.reporters:
            reporter.end()
        # if self.aborted:
        #     print("\nABORTED: By user.")
        failed = ((failed_count > 0) or self.aborted or
                  (len(self.undefined_steps) > undefined_steps_initial_size))
        return failed

    def run(self):
        with self.path_manager:
            self.setup_paths()
            return self.run_with_paths()

if __name__ == "__main__":
    set_environment_data(init_context())
    custom_behave = CustomBehave()
    custom_behave.run()


