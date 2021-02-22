import random

from .base import CalculatorBase


class RandomCalculator(CalculatorBase):
    def calculate(self, digits: list):
        return random.choice(digits)

    def description(self):
        return 'Selects one of the digits randomly'
