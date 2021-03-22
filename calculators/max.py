from .base import CalculatorBase


class MaxCalculator(CalculatorBase):
    def calculate(self, digits: list):
        if not digits:
            return 0
        return max(digits)

    def description(self):
        return 'Calculates max of digits'
