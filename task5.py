from helper import Helper


class Task5:

    __task_number = 5

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дана квадратная вещественная матрица размерности n. Найти количество нулевых элементов,'
              '\nстоящих: выше главной диагонали; ниже главной диагонали')
        n = helper.set_natural_number('Введите размерность матрицы n', range(3, 10))
        random_matrix = helper.set_random_matrix(n, n, range(-10, 10))
        helper.print_matrix(random_matrix)
        print('----------------------------------------------------------')
        self.__calculate_variant_a(random_matrix)
        self.__calculate_variant_b(random_matrix)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __calculate_variant_a(matrix: [[]]):
        try:
            count = 0
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if j >= i:
                        print('[X]', end='')
                        if matrix[i][j] == 0:
                            count += 1
                    else:
                        print('[ ]', end='')
                if i == len(matrix) - 1:
                    print(f' Количество нулевых элементов = {count}\n')
                else:
                    print('')
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __calculate_variant_b(matrix: [[]]):
        try:
            count = 0
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    if j <= i:
                        print('[X]', end='')
                        if matrix[i][j] == 0:
                            count += 1
                    else:
                        print('[ ]', end='')
                if i == len(matrix) - 1:
                    print(f' Количество нулевых элементов = {count}\n')
                else:
                    print('')
        except Exception as e:
            print(f'Ошибка: {e}')
