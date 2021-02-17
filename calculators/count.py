from .base import CalculatorBase


class CountCalculator(CalculatorBase):
    def calculate(self, digits: list):
        return len(digits)

    def description(self):
        return 'Calculates count of digits'
