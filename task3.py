from helper import Helper


class Task3:

    __task_number = 3

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Составить вектор, элементы которого равны среднему арифметическому каждой строки прямоугольной матрицы.')
        m = helper.set_natural_number('m (строка)')
        n = helper.set_natural_number('n (столбец)')
        random_matrix = helper.set_random_matrix(m, n, range(-100, 100))
        helper.print_matrix(random_matrix)
        print('----------------------------------------------------------')
        print(f'Вектор из ср. арифметического строк: {self.__get_average_vector(random_matrix)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_average_vector(matrix: [[]]) -> []:
        try:
            vector = []
            for row in matrix:
                vector.append(round(sum(row) / len(row), 2))
            return vector
        except:
            print('Ошибка')
