from abc import ABC, abstractmethod


class ProcessorBase(ABC):
    @abstractmethod
    def process(self, **kwargs):
        pass

    @abstractmethod
    def description(self):
        pass
