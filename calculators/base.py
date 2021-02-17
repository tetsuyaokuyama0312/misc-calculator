from abc import ABC, abstractmethod


class CalculatorBase(ABC):
    @abstractmethod
    def calculate(self, digits: list):
        pass

    @abstractmethod
    def description(self):
        pass
