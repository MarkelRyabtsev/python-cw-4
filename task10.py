import copy

from helper import Helper


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
        print('Если в массиве присутствуют отрицательные элементы, заменить их значения средним арифметическим массива.'
              '\nПодсчитать и вывести количество совпадающих элементов массива')
        n = helper.set_natural_number('Введите размерность массива n', range(1, 11))
        random_array = helper.set_random_array(n, range(-n, n))
        print('----------------------------------------------------------')
        print(f'Исходный массив: {random_array}')
        print(f'После замены отрицательных эл.: {self.__get_least_distant_element(random_array)}')
        self.__show_duplicates(random_array)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_least_distant_element(array: []) -> []:
        try:
            average = round(sum(array) / len(array), 2)
            new_array = copy.deepcopy(array)
            for i in range(0, len(new_array)):
                if new_array[i] < 0:
                    new_array[i] = average
            return new_array
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __show_duplicates(array: []):
        try:
            duplicates = dict()
            for i in range(0, len(array)):
                count = 1
                for j in range(1, len(array)):
                    if array[j] == array[i] and i != j:
                        count += 1
                        duplicates[array[j]] = count
            if len(duplicates) != 0:
                print(f'Количество совпадающих элементов:')
                for key in duplicates.keys():
                    print(f'{key}: {duplicates[key]}')
            else:
                print('Повторений нет.')
        except Exception as e:
            print(f'Ошибка: {e}')
