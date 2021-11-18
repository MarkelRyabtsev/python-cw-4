from helper import Helper


class Task16:

    __task_number = 16

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дан двумерный массив. В каждой строке все его положительные элементы переписать (сохраняя порядок)'
              '\nв начало строки, а отрицательные элементы - в конец массива. Дополнительный массив не использовать')
        m = helper.set_natural_number('m (строка)')
        n = helper.set_natural_number('n (столбец)')
        random_matrix = helper.set_random_matrix(m, n, range(-100, 100))
        helper.print_matrix(random_matrix)
        print('----------------------------------------------------------')
        print('После сортировки:')
        helper.print_matrix(self.__get_sorted_matrix(random_matrix))
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_sorted_matrix(matrix: [[]]) -> [[]]:
        try:
            for row in matrix:
                if all(item < 0 for item in row):
                    continue
                if any(item < 0 for item in row):
                    row.sort(key=lambda x: x < 0)
            return matrix
        except Exception as e:
            print(f'Ошибка: {e}')
