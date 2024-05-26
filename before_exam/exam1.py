class Trojkat(object):
    H = 1

    def __init__(self, A=100):
        self.A = A

    def poletrojkata(self):
        return self.A * self.H * 1 / 2

    def __sub__(self, other):
        return self.poletrojkata() - other.poletrojkata()


class GraniastoslupTrojkatny(Trojkat):
    def __init__(self, A, H):
        super().__init__(A)
        self._H = H

    def polegraniastoslupa(self):
        return super().poletrojkata() + 4 * self.A * self._H


def multi(*args):
    if len(args) == 1 and type(args[0]) is list:
        power = map(lambda x: x * x if x % 2 != 0 else x, args[0])
    elif len(args) > 1:
        i = 0
        ilo = 1
        while i < len(args):
            ilo *= args[i]
            i += 1
    else:
        return "Wrong shit"


def decorator(func):
    def wrapper(operation, a, b):
        if operation == "+":
            func(a, b)
        elif operation == "-":
            return a - b
    return wrapper


@decorator
def calculator(a, b):
    return a + b
