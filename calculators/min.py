from .base import CalculatorBase


class MinCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return min(digits)

    def description(self):
        return 'Calculates min of digits'
