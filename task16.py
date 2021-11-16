import math
from helper import Helper, Range


class Task16:

    __task_number = 16

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить z = (3*x^2 - √cos(q^3))/(ln(q + a)t). Параметр x изменяется от x=xн=0.2 до x=xк=0.6'
              '\nс шагом h=0.1. a, q, t – константы. Использовать цикл while или repeat')
        a = helper.set_real_number('a')
        q = helper.set_real_number('q')
        t = helper.set_real_number('t')
        x_start = 0.2
        x_stop = 0.6
        x_step = 0.1
        x_range = Range(
            x_start,
            x_stop,
            x_step
        )
        print('----------------------------------------------------------')
        values = self.__get_dict_values(x_range, a, q, t)
        for value in values:
            print(f'При x = {value}: z = {values[value]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_dict_values(self, x_range: Range, a: float, q: float, t: float) -> dict[float, float]:
        try:
            dict_values = dict()
            x = x_range.start
            while x <= x_range.stop:
                dict_values[round(x, 1)] = self.__get_z(x, a, q, t)
                x += x_range.step
            return dict_values
        except:
            print('Ошибка входных данных')
            return dict()

    @staticmethod
    def __get_z(x: float, a: float, q: float, t: float) -> float:
        try:
            return round((3 * (x ** 2) - math.sqrt(math.cos(q ** 3))) / (math.log((q + a) * t, math.e)), 4)
        except:
            raise Exception
