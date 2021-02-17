from abc import ABC, abstractmethod


class Descriptable(ABC):
    @abstractmethod
    def description(self):
        pass
