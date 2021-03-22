from statistics import variance

from .base import CalculatorBase


class VarianceCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return variance(digits)

    def description(self):
        return 'Calculates variance of digits'
