from statistics import mean

from .base import CalculatorBase


class MeanCalculator(CalculatorBase):
    def calculate(self, digits: list):
        return mean(digits) if digits else 0

    def description(self):
        return 'Calculates mean of digits'
