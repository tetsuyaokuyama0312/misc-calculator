from abc import abstractmethod

from descriptable import Descriptable


class ProcessorBase(Descriptable):
    @abstractmethod
    def process(self, **kwargs):
        pass
