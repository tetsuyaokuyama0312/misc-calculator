from .base import ProcessorBase


class HelpProcessor(ProcessorBase):
    def process(self, **kwargs):
        calculators = kwargs['calculators']
        processors = kwargs['processors']
        exit_commands = kwargs['exit_commands']

        print('--------------------')
        print('Calculation commands')
        for cmd, calculator in calculators.items():
            print(cmd, end=': ')
            print(calculator.description())

        print()

        print('Other commands')
        for cmd, processor in processors.items():
            print(cmd, end=': ')
            print(processor.description())

        print()

        print('Exit commands')
        print(', '.join(exit_commands), end=': ')
        print('Exits this application')

        print('--------------------')

    def description(self):
        return 'Prints help text'
