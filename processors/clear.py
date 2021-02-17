from .base import ProcessorBase


class ClearProcessor(ProcessorBase):
    def process(self, **kwargs):
        digits = kwargs['digits']
        digits.clear()

    def description(self):
        return 'Clears digits'
