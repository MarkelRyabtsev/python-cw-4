import math
from helper import Helper, Range


class Task13:

    __task_number = 13

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print('Вычислить y = (sin^2(z+a)^3)/(t√e^(a+2q)). Параметр z изменяется от z=zн=0.5 до z=zк=1'
              '\nс шагом h=0.1. a, q, t – константы. Использовать цикл while или repeat')
        a = helper.set_real_number('a')
        q = helper.set_real_number('q')
        t = helper.set_real_number('t')
        z_start = 0.5
        z_stop = 1.0
        z_step = 0.1
        z_range = Range(
            z_start,
            z_stop,
            z_step
        )
        print('----------------------------------------------------------')
        values = self.__get_dict_values(z_range, a, q, t)
        for value in values:
            print(f'При z = {value}: y = {values[value]}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    def __get_dict_values(self, z_range: Range, a: float, q: float, t: float) -> dict[float, float]:
        try:
            dict_values = dict()
            z = z_range.start
            while z <= z_range.stop:
                dict_values[round(z, 1)] = self.__get_w(z, a, q, t)
                z += z_range.step
            return dict_values
        except:
            print('Ошибка входных данных')
            return dict()

    @staticmethod
    def __get_w(z: float, a: float, q: float, t: float) -> float:
        try:
            return round((math.sin(pow(z + a, 3)) ** 2) / (t * math.sqrt(math.pow(math.e, a + 2 * q))), 4)
        except:
            raise Exception
