from helper import Helper


class Task13:

    __task_number = 13

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print('Найти в массиве наибольшее число повторений элементов.'
              '\nВывести значение элемента и количество его повторений')
        n = helper.set_natural_number('Введите размерность массива n', range(1, 11))
        random_array = helper.set_random_array(n, range(-n, n))
        print('----------------------------------------------------------')
        print(random_array)
        self.__show_duplicates(random_array)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __show_duplicates(array: []):
        try:
            duplicates = dict()
            for i in range(0, len(array)):
                count = 1
                for j in range(1, len(array)):
                    if array[j] == array[i] and (i != j or i == len(array) - 1):
                        count += 1
                        duplicates[array[j]] = count
            if len(duplicates) != 0:
                sorted_dict = dict(sorted(duplicates.items(), key=lambda item: item[1], reverse=True))
                first_key = next(iter(sorted_dict))
                max_count = sorted_dict[first_key]
                dict_with_max_duplicates = {key: value for key, value in sorted_dict.items() if value == max_count}
                print(f'Наибольшее число повторений у:')
                for duplicate in dict_with_max_duplicates:
                    print(f'[{duplicate}]: {dict_with_max_duplicates[duplicate]}')
            else:
                print('Повторений нет.')
        except Exception as e:
            print(f'Ошибка: {e}')
