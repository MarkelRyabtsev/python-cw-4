from helper import Helper


class Task8:

    __task_number = 8

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дана вещественная матрица размерности n * m. Сформировать вектор b, '
              '\nв котором элементы вычисляются как:'
              '\n- произведение элементов соответствующих строк;'
              '\n- среднее арифметическое соответствующих столбцов;'
              '\n- разность наибольших и наименьших элементов соответствующих строк;'
              '\n- значения первых отрицательных элементов в столбце')
        m = helper.set_natural_number('m (строка)')
        n = helper.set_natural_number('n (столбец)')
        random_matrix = helper.set_random_matrix(m, n, range(-100, 100))
        helper.print_matrix(random_matrix)
        print('----------------------------------------------------------')
        print(f'Вектор из произв. элем. строк: {self.__get_product_vector(random_matrix)}')
        print(f'Вектор из ср. арифметического столбцов: {self.__get_average_vector(random_matrix)}')
        print(f'Вектор из разности наибольших и наименьших эл. строк: {self.__get_diff_max_min_vector(random_matrix)}')
        print(f'Вектор из значений первых отрицательных эл. в столбце: '
              f'{self.__get_first_negative_numbers_vector(random_matrix)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

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
            for column in range(0, len(matrix[0])):
                sum_column = 0
                for row in range(0, len(matrix)):
                    sum_column += matrix[row][column]
                vector.append(round(sum_column / len(matrix), 2))
            return vector
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_diff_max_min_vector(matrix: [[]]) -> []:
        try:
            vector = []
            for row in matrix:
                vector.append(max(row) - min(row))
            return vector
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_first_negative_numbers_vector(matrix: [[]]) -> []:
        try:
            vector = []
            for column in range(0, len(matrix[0])):
                for row in range(0, len(matrix)):
                    if matrix[row][column] < 0:
                        vector.append(matrix[row][column])
                        break
            return vector
        except Exception as e:
            print(f'Ошибка: {e}')
