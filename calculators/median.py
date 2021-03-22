from statistics import median

from .base import CalculatorBase


class MedianCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return median(digits)

    def description(self):
        return 'Calculates median of digits'
