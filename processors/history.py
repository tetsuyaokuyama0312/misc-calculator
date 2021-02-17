from .base import ProcessorBase


class HistoryProcessor(ProcessorBase):
    def process(self, **kwargs):
        history = kwargs['history']
        if not history:
            print('No history')
            return
        for hist in history:
            print(hist)

    def description(self):
        return 'Prints history'
