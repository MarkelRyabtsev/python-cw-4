from helper import Helper


class Task9:

    __task_number = 9

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дано вещественное число r и массив размера n.'
              '\nНайти элемент массива, который наиболее и наименее близок к данному числу')
        n = helper.set_natural_number('Введите размерность массива n', range(1, 11))
        r = helper.set_natural_number('Число для поиска r', range(-n, n), True)
        random_array = helper.set_random_array(n, range(-n, n), True)
        print(random_array)
        print('----------------------------------------------------------')
        print(f'Наиболее близок к {r} : {self.__get_least_distant_element(random_array, r)}')
        print(f'Наименее близок к {r} : {self.__get_most_distant_element(random_array, r)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_least_distant_element(array: [], r: int) -> int:
        try:
            element = array[0]
            for i in array:
                if abs(i - r) < abs(element - r):
                    element = i
            return element
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_most_distant_element(array: [], r: int) -> int:
        try:
            element = array[0]
            for i in array:
                if abs(i - r) > abs(element - r):
                    element = i
            return element
        except Exception as e:
            print(f'Ошибка: {e}')
