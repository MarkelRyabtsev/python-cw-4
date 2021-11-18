import copy

from helper import Helper


class Task15:

    __task_number = 15

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Заменить положительные элементы матрицы нулями, отрицательные – единицами.'
              '\nПереписать массив таким образом, чтобы нулевые элементы стояли в его конце,'
              '\nно при этом сохранялась очередность других')
        m = helper.set_natural_number('m (строка)')
        n = helper.set_natural_number('n (столбец)')
        random_matrix = helper.set_random_matrix(m, n, range(-n, n))
        helper.print_matrix(random_matrix)
        print('----------------------------------------------------------')
        print('После замены:')
        changed_matrix = self.__get_changed_matrix(random_matrix)
        helper.print_matrix(changed_matrix)
        print('После сортировки:')
        sorted_matrix = self.__get_sorted_matrix(random_matrix)
        helper.print_matrix(sorted_matrix)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_changed_matrix(matrix: [[]]) -> [[]]:
        try:
            new_matrix = copy.deepcopy(matrix)
            for i in range(0, len(new_matrix)):
                for j in range(0, len(new_matrix[i])):
                    if new_matrix[i][j] > 0:
                        new_matrix[i][j] = 0
                    else:
                        new_matrix[i][j] = 1
            return new_matrix
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_sorted_matrix(matrix: [[]]) -> [[]]:
        try:
            new_matrix = copy.deepcopy(matrix)
            for row in new_matrix:
                if all(item < 0 for item in row):
                    continue
                if any(item < 0 for item in row):
                    row.sort(key=lambda x: x == 0)
            return new_matrix
        except Exception as e:
            print(f'Ошибка: {e}')
