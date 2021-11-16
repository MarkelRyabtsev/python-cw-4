import math
from helper import Helper


class Task8:

    __task_number = 8

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дано действительное число x, натуральное n. Вычислить: x^1/1! + ... + x^n/n!')
        x = helper.set_real_number('x', False)
        n = helper.set_natural_number('n')
        print('----------------------------------------------------------')
        self.__print_formula(x, n)
        print(f' = {self.__calculate(x, n)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_formula(x: float, n: int):
        count = 1
        while count <= n:
            print(f'({x}^{count}/{count}!)', end='')
            count += 1
            if count <= n:
                print(' + ', end='')

    @staticmethod
    def __calculate(x: float, n: int) -> float:
        value = 0
        count = 1
        while count <= n:
            value += math.pow(x, count)/math.factorial(count)
            count += 1

        return round(value, 2)
