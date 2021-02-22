from typing import NamedTuple

from calculators import *
from processors import *


class Command(NamedTuple):
    name: str
    synonyms: tuple

    def __str__(self):
        cmds = (self.name,) + self.synonyms
        return ', '.join(cmds)

    def match(self, data: str):
        return self.name == data or data in self.synonyms

    @classmethod
    def of(cls, name: str, *synonyms: str):
        return Command(name, tuple(synonyms))


class History(NamedTuple):
    operation: str
    digits: list
    result: float

    def __str__(self):
        if self.digits is None:
            return self.operation
        return f'{self.operation} of {self.digits} is {self.result}'

    @classmethod
    def of(cls, operation: str, digits: list = None, result: float = None):
        if digits is not None:
            digits = digits.copy()
        return History(operation, digits, result)


# Dictionary that associates commands with calculators
CALCULATORS = {
    Command.of('sum', 'total'): SumCalculator(),
    Command.of('mean', 'average', 'avg'): MeanCalculator(),
    Command.of('median', 'med'): MedianCalculator(),
    Command.of('max'): MaxCalculator(),
    Command.of('min'): MinCalculator(),
    Command.of('count', 'cnt', 'length', 'len'): CountCalculator(),
    Command.of('random', 'rand'): RandomCalculator(),
}

# Dictionary that associates commands with processors
PROCESSORS = {
    Command.of('check', 'check-digits', 'digits'): CheckProcessor(),
    Command.of('clear', 'clr', 'reset', 'rst'): ClearProcessor(),
    Command.of('help', 'h'): HelpProcessor(),
    Command.of('history', 'hist'): HistoryProcessor(),
}

EXIT_COMMANDS = {
    'exit',
    'bye',
    'stop',
    'end',
}


def is_exit_command(data: str):
    return data in EXIT_COMMANDS


def is_calc_command(data: str):
    return any(cmd.match(data) for cmd in CALCULATORS)


def is_process_command(data: str):
    return any(cmd.match(data) for cmd in PROCESSORS)


def is_command(data: str):
    return is_calc_command(data) or is_process_command(data)


def get_calculator(cmd: str):
    command = first(lambda c: c.match(cmd), CALCULATORS)
    return CALCULATORS[command]


def get_processor(cmd: str):
    command = first(lambda p: p.match(cmd), PROCESSORS)
    return PROCESSORS[command]


def first(pred, lst):
    return next(filter(pred, lst), None)


def process(cmd: str, digits: list, history: list):
    if is_calc_command(cmd):
        result = get_calculator(cmd).calculate(digits)
        print(result)
        history.append(History.of(cmd, digits, result))

    elif is_process_command(cmd):
        get_processor(cmd).process(cmd=cmd, digits=digits, history=history, calculators=CALCULATORS,
                                   processors=PROCESSORS, exit_commands=EXIT_COMMANDS)
        history.append(History.of(cmd))

    else:
        raise ValueError('cmd must be command')


def try_append_as_digit(digits: list, data: str):
    try:
        digits.append(int(data))
        return True
    except ValueError:
        try:
            digits.append(float(data))
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    history = []
    digits = []

    print('Please input a digit or command')
    while True:
        data = input('$ ')
        if not data:
            continue

        data = data.lower()
        if is_exit_command(data):
            break
        elif is_command(data):
            process(data, digits, history)
        else:
            if not try_append_as_digit(digits, data):
                print('The inputted data cannot be interpreted as a digit or command')
