from helper import Helper


class Task11:

    __task_number = 11

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан двухмерный массив A[1..m,1..n]. Написать программу построения одномерного массива B[1..m],'
              '\nэлементы которого соответственно равны:'
              '\nа) суммам элементов строк,'
              '\nб) произведениям элементов строк,'
              '\nв) наименьшим средних арифметических элементов строк.')
        m = helper.set_natural_number('m (строка)')
        n = helper.set_natural_number('n (столбец)')
        random_matrix = helper.set_random_matrix(m, n, range(-100, 100))
        helper.print_matrix(random_matrix)
        print('----------------------------------------------------------')
        print(f'а) {self.__get_sum_vector(random_matrix)}')
        print(f'б) {self.__get_product_vector(random_matrix)}')
        print(f'в) {self.__get_average_vector(random_matrix)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_sum_vector(matrix: [[]]) -> []:
        try:
            vector = []
            for row in matrix:
                vector.append(sum(row))
            return vector
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_product_vector(matrix: [[]]) -> []:
        try:
            vector = []
            for row in matrix:
                product = 1
                for i in row:
                    product *= i
                vector.append(product)
            return vector
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_average_vector(matrix: [[]]) -> []:
        try:
            vector = []
            for row in matrix:
                vector.append(round(sum(row) / len(row), 2))
            return vector
        except Exception as e:
            print(f'Ошибка: {e}')
