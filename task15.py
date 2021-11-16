import math
from helper import Helper


class Task15:

    __task_number = 15

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить приближенно значение бесконечной суммы: 1 + x^1/1! + x^2/2! + x^3/3! = ... = e^x'
              '\nНужное приближение считается полученным, если вычислена сумма нескольких первых слагаемых,'
              '\nи очередное слагаемое оказалось по модулю меньше данного положительного числа e')
        x = helper.set_natural_number('x')
        epc = helper.set_degree_of_accuracy('Введите степень точности')
        print('----------------------------------------------------------')
        self.__calculate(x, epc, helper)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __calculate(x: int, epc: float, helper: Helper):
        n = 1
        exact_value = math.e ** x
        epc_str = helper.float_to_str(epc)
        count_symbols = len(epc_str.split(".")[1])
        total_sum = 1.0
        while True:
            a = x ** n / math.factorial(n)
            if abs(a) < epc:
                break
            n += 1
            total_sum += a
        helper.show_degree_of_accuracy_result(exact_value, round(total_sum, count_symbols), epc_str)
