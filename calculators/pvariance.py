from statistics import pvariance

from .base import CalculatorBase


class ParentVarianceCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return pvariance(digits)

    def description(self):
        return 'Calculates parent variance of digits'
