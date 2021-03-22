from statistics import pstdev

from .base import CalculatorBase


class ParentStdCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return pstdev(digits)

    def description(self):
        return 'Calculates parent standard deviation of digits'
