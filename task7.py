from helper import Helper


class Task7:

    __task_number = 7

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Дана последовательность   100 различных целых чисел. Найти сумму чисел этой последовательности,'
              '\nрасположенных между максимальным и минимальным числами (в сумму можно включить и сами эти два числа)')
        random_array = helper.set_random_array(100, range(-100, 100), True)
        print(random_array)
        print('----------------------------------------------------------')
        sum_between_max_and_min = self.__get_sum_between_max_and_min(random_array)
        print(f'Сумма элементов между макс. и мин. значениями = {sum_between_max_and_min}')
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __get_sum_between_max_and_min(array: []) -> int:
        try:
            sum_between_max_and_min = 0
            trimmed_array = []
            max_value = max(array)
            min_value = min(array)
            print(f'Минимальное значение: {min_value}')
            print(f'Максимальное значение: {max_value}')
            max_index = array.index(max_value)
            min_index = array.index(min_value)
            if max_index > min_index:
                for i in range(0, len(array)):
                    if min_index <= i <= max_index:
                        trimmed_array.append(array[i])
                        sum_between_max_and_min += array[i]
            else:
                for i in range(0, len(array)):
                    if max_index <= i <= min_index:
                        trimmed_array.append(array[i])
                        sum_between_max_and_min += array[i]
            print(trimmed_array)
            return sum_between_max_and_min
        except:
            print('Ошибка')
