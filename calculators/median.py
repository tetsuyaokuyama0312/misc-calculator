from statistics import median

from .base import CalculatorBase


class MedianCalculator(CalculatorBase):
    def calculate(self, digits: list):
        return median(digits) if digits else 0

    def description(self):
        return 'Calculates median of digits'
