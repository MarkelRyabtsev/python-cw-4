from helper import Helper


class Task2:

    __task_number = 2

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('В массиве из n элементов найти сумму элементов массива, среднее арифметическое чисел,'
              '\n входящих в массив, произведение положительных элементов')
        n = helper.set_natural_number('Введите размерность массива n', range(1, 10))
        random_array = helper.set_random_array(n, range(-100, 100))
        print(random_array)
        print('----------------------------------------------------------')
        sum_array = self.__get_sum(random_array)
        average_value = self.__get_average_value(random_array)
        product_of_positive_numbers = self.__get_product_of_positive_numbers(random_array)
        print(f'Сумма элементов массива = {sum_array}')
        print(f'Среднее арифметическое чисел = {average_value}')
        print(f'Произведение положительных элементов = {product_of_positive_numbers}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_sum(array: []) -> int:
        try:
            return sum(array)
        except:
            print('Ошибка')

    @staticmethod
    def __get_average_value(array: []) -> float:
        try:
            return sum(array) / len(array)
        except:
            print('Ошибка')

    @staticmethod
    def __get_product_of_positive_numbers(array: []) -> int:
        try:
            positive_values = [i for i in array if i > 0]
            product = 1
            for value in positive_values:
                product *= value
            return product
        except:
            print('Ошибка')
