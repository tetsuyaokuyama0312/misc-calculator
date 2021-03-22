from statistics import stdev

from .base import CalculatorBase


class StdCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return stdev(digits)

    def description(self):
        return 'Calculates standard deviation of digits'
