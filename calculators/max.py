from .base import CalculatorBase


class MaxCalculator(CalculatorBase):
    def calculate(self, digits: list):
        return max(digits) if digits else 0

    def description(self):
        return 'Calculates max of digits'
