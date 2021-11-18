from helper import Helper


class Task1:

    __task_number = 1

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить X=m/(n-m), где m - сумма квадратов отрицательных элементов первого вектора,'
              '\nn - сумма квадратов отрицательных элементов второго вектора')
        vector_1 = helper.set_random_array(10, range(-10, 10))
        vector_2 = helper.set_random_array(10, range(-10, 10))
        print('----------------------------------------------------------')
        print(f'Вектор 1: {vector_1}')
        print(f'Вектор 2: {vector_2}')
        m = self.__get_sum_of_pow(vector_1)
        n = self.__get_sum_of_pow(vector_2)
        print(f'm = {m}')
        print(f'n = {n}')
        print(f'X = m/(n-m) = {m}/({n}-{m}) = {self.__get_x(m, n)}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_sum_of_pow(vector: [int]) -> int:
        try:
            if len(vector) == 0:
                return 0
            negative_values = [i for i in vector if i < 0]
            return sum([i ** 2 for i in negative_values])
        except Exception as e:
            print(f'Ошибка: {e}')

    @staticmethod
    def __get_x(m: int, n: int) -> float:
        try:
            return round(m / (n - m), 2)
        except Exception as e:
            print(f'Ошибка: {e}')
