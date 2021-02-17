from .base import CalculatorBase


class MinCalculator(CalculatorBase):
    def calculate(self, digits: list):
        return min(digits) if digits else 0

    def description(self):
        return 'Calculates min of digits'
