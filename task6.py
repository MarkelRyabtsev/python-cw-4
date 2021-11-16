from helper import Helper


class Task6:

    __task_number = 6

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('В массиве из n элементов найти количество нулевых элементов массива, сумму отрицательных и'
              '\nпроизведение положительных элементов массива.')
        n = helper.set_natural_number('Введите размерность массива n', range(1, 11))
        random_array = helper.set_random_array(n, range(-10, 10))
        print(random_array)
        print('----------------------------------------------------------')
        zero_count = self.__get_zero_count(random_array)
        sum_of_negative = self.__get_sum_of_negative(random_array)
        product_of_positive_numbers = self.__get_product_of_positive_numbers(random_array)
        print(f'Количество нулевых элементов = {zero_count}')
        print(f'Сумма отрицательных элементов = {sum_of_negative}')
        print(f'Произведение положительных элементов = {product_of_positive_numbers}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_zero_count(array: []) -> int:
        try:
            count = 0
            for i in array:
                if i == 0:
                    count += 1
            return count
        except:
            print('Ошибка')

    @staticmethod
    def __get_sum_of_negative(array: []) -> int:
        try:
            negative_values = [i for i in array if i < 0]
            return sum(negative_values)
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
