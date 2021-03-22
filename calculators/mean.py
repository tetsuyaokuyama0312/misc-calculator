from statistics import mean

from .base import CalculatorBase


class MeanCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return mean(digits)

    def description(self):
        return 'Calculates mean of digits'
