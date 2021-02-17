from .base import CalculatorBase


class SumCalculator(CalculatorBase):
    def calculate(self, digits: list):
        return sum(digits)

    def description(self):
        return 'Calculates sum of digits'
