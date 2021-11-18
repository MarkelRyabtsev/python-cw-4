import copy

from helper import Helper


class Task12:

    __task_number = 12

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Расположить элементы массива в обратном порядке (первый элемент меняется с последним,'
              '\nвторой - с предпоследним и т.д. до середины;'
              '\nесли массив содержит нечетное количество элементов, то средний остается без изменения).')
        n = helper.set_natural_number('Введите размерность массива n', range(1, 11))
        random_array = helper.set_random_array(n, range(-n, n))
        print('----------------------------------------------------------')
        print(f'Исходный массив: {random_array}')
        print(f'После перестановки: {self.__get_changed_array(random_array, helper)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_changed_array(array: [], helper: Helper) -> []:
        try:
            new_array = copy.deepcopy(array)
            for i in range(0, len(new_array)):
                new_array[i], new_array[len(new_array) - 1 - i] = helper.swap_items(
                    new_array[i],
                    new_array[len(new_array) - 1 - i]
                )
                if i == round((len(new_array) - 1) / 2):
                    break
            return new_array
        except Exception as e:
            print(f'Ошибка: {e}')
