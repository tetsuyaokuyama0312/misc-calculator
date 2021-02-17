from abc import abstractmethod

from descriptable import Descriptable


class CalculatorBase(Descriptable):
    @abstractmethod
    def calculate(self, digits: list):
        pass
