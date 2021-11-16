from helper import Helper


class Task12:

    __task_number = 12

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('На промежутке от 1 до M найти все числа Армстронга. Натуральное число из n цифр называется'
              '\nчислом Армстронга, если сумма его цифр, возведенных в n-ю степень, равна самому числу')
        m = helper.set_natural_number('M')
        print('----------------------------------------------------------')
        number_list = self.__get_armstrong_numbers(m)
        self.__print_numbers(number_list, m)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __print_numbers(number_list: list[int], m: int):
        if len(number_list) > 0:
            print(f'Числа Армстронга в диапозоне [1, {m}]:'
                  f'\n{number_list}')

    @staticmethod
    def __get_armstrong_numbers(m: int) -> list[int]:
        number_list = []
        for number in range(1, m + 1, 1):
            checked_sum = sum(
                map(
                    lambda x: int(x) ** len(str(number)), str(number)
                )
            )
            if checked_sum == number:
                number_list.append(number)
        return number_list
