import math
from helper import Helper, Range


class Task10:

    __task_number = 10

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить t = (b^2 + √|q|)/(cos^2(x) + b*ln(y)) Параметр x изменяется от х=хн=1 до х=хк=5'
              '\nс шагом h=1. b, q, y – константы. Использовать цикл while или repeat')
        b = helper.set_real_number('b')
        q = helper.set_real_number('q')
        y = helper.set_real_number('y')
        x_start = 1
        x_stop = 5
        x_step = 1
        x_range = Range(
            x_start,
            x_stop,
            x_step
        )
        print('----------------------------------------------------------')
        values = self.__get_dict_values(x_range, b, q, y)
        for value in values:
            print(f'При x = {value}: t = {values[value]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_dict_values(self, x_range: Range, b: float, q: float, y: float) -> dict[float, float]:
        try:
            dict_values = dict()
            x = x_range.start
            while x <= x_range.stop:
                dict_values[round(x, 1)] = self.__get_w(x, b, q, y)
                x += x_range.step
            return dict_values
        except:
            print('Ошибка входных данных')
            return dict()

    @staticmethod
    def __get_w(x: float, b: float, q: float, y: float) -> float:
        try:
            return round((b ** 2 + math.sqrt(abs(q))) / (math.cos(x) ** 2 + b * math.log(y, math.e)), 4)
        except:
            raise Exception
