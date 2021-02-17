from .base import ProcessorBase


class CheckProcessor(ProcessorBase):
    def process(self, **kwargs):
        digits = kwargs['digits']
        print(f'digits is {digits}')

    def description(self):
        return 'Prints digits'
