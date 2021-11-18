import copy

from helper import Helper


class Task14:

    __task_number = 14

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('В массиве поменять местами элементы, стоящие на нечетных местах,'
              '\nс элементами, стоящими на четных местах')
        n = helper.set_natural_number('Введите размерность массива n', range(1, 11))
        random_array = helper.set_random_array(n, range(-n, n))
        print('----------------------------------------------------------')
        print(f'Исходный массив: {random_array}')
        print(f'После перестановки: {self.__get_swapped_array(random_array, helper)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_swapped_array(array: [], helper: Helper) -> []:
        try:
            new_array = copy.deepcopy(array)
            for i in range(0, len(new_array), 2):
                if i == (len(new_array) - 1):
                    break
                new_array[i], new_array[i + 1] = helper.swap_items(
                    new_array[i],
                    new_array[i + 1]
                )
            return new_array
        except Exception as e:
            print(f'Ошибка: {e}')
