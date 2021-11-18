from helper import Helper


class Task4:

    __task_number = 4

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Найти наибольший элемент, расположенный в заштрихованной части матрицы размерности n*n')
        n = helper.set_natural_number('Введите размерность матрицы n', range(3, 10))
        random_matrix = helper.set_random_matrix(n, n, range(-100, 100))
        helper.print_matrix(random_matrix)
        print('----------------------------------------------------------')
        self.__calculate_variant_a(random_matrix)
        self.__calculate_variant_b(random_matrix)
        self.__calculate_variant_c(random_matrix)
        self.__calculate_variant_d(random_matrix)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __calculate_variant_a(matrix: [[]]):
        try:
            max_value = None
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if j >= i:
                        print('[X]', end='')
                        if max_value is None or matrix[i][j] > max_value:
                            max_value = matrix[i][j]
                    else:
                        print('[ ]', end='')
                if i == len(matrix) - 1:
                    print(f' Максимальное значение в области = {max_value}\n')
                else:
                    print('')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __calculate_variant_b(matrix: [[]]):
        try:
            max_value = None
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if j <= i:
                        print('[X]', end='')
                        if max_value is None or matrix[i][j] > max_value:
                            max_value = matrix[i][j]
                    else:
                        print('[ ]', end='')
                if i == len(matrix) - 1:
                    print(f' Максимальное значение в области = {max_value}\n')
                else:
                    print('')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __calculate_variant_c(matrix: [[]]):
        try:
            max_value = None
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if j <= len(matrix) - i - 1:
                        print('[X]', end='')
                        if max_value is None or matrix[i][j] > max_value:
                            max_value = matrix[i][j]
                    else:
                        print('[ ]', end='')
                if i == len(matrix) - 1:
                    print(f' Максимальное значение в области = {max_value}\n')
                else:
                    print('')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __calculate_variant_d(matrix: [[]]):
        try:
            max_value = None
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if j >= len(matrix) - i - 1:
                        print('[X]', end='')
                        if max_value is None or matrix[i][j] > max_value:
                            max_value = matrix[i][j]
                    else:
                        print('[ ]', end='')
                if i == len(matrix) - 1:
                    print(f' Максимальное значение в области = {max_value}')
                else:
                    print('')
        except Exception as e:
            print(f'Ошибка: {e}')
