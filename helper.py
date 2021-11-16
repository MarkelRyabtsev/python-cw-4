import random


class Range:

    def __init__(self, start: float, stop: float, step: float):
        self.start = start
        self.stop = stop
        self.step = step


class Helper:

    @staticmethod
    def show_degree_of_accuracy_result(exact_value: float, approximate_value: float, epc: str):
        print(f'Точное значение = {exact_value}')
        print(f'Степень точности = {epc}')
        print(f'Приблеженное значение = {approximate_value}')

    @staticmethod
    def set_degree_of_accuracy(description: str) -> float:
        while True:
            try:
                value = float(input(f'{description} : '))
                if 0 < value < 1:
                    return value
                else:
                    print(f'Введенное число должно быть в пределах от 0 до 1')
                    continue
            except:
                print('Введенное число должно быть в пределах от 0 до 1')
                continue

    @staticmethod
    def set_real_number(description: str, only_positive: bool = False, not_equal: float = None) -> float:
        while True:
            try:
                value = float(input(f'{description} : '))
                if only_positive:
                    if value < 0:
                        print(f'Введенное число должно быть больше 0!')
                        continue
                if not_equal is not None and value == not_equal:
                    print(f'Введенное число должно отличаться от {not_equal}!')
                    continue
                return value
            except:
                print('Введенное значение не является вещественным числом, повторите!')
                continue

    @staticmethod
    def set_natural_number(description: str, numbers_range: range = None) -> int:
        while True:
            try:
                value = int(input(f'{description} : '))
                if value < 1:
                    print('Число должно быть больше 0!')
                    continue
                if numbers_range is not None and value not in numbers_range:
                    print(f'Введенное число должно быть в диапозоне от {numbers_range.start} до {numbers_range.stop}!')
                    continue
                return value
            except:
                print('Введенное значение не является натуральным числом, повторите!')
                continue

    @staticmethod
    def set_random_array(n: int, values_range: range, is_uniq: bool = False) -> []:
        random_array = []
        for i in range(0, n):
            random_value = random.randint(values_range.start, values_range.stop)
            if is_uniq:
                while True:
                    if random_value not in random_array:
                        break
                    else:
                        random_value = random.randint(values_range.start, values_range.stop)
            random_array.insert(i, random_value)
        return random_array

    @staticmethod
    def set_random_matrix(m: int, n: int, values_range: range) -> [[]]:
        random_array = []
        for i in range(0, m):
            row = []
            for a in range(0, n):
                row.insert(a, random.randint(values_range.start, values_range.stop))
            random_array.insert(i, row)
        return random_array

    @staticmethod
    def print_matrix(matrix: [[]]):
        for row in matrix:
            print(row)

    @staticmethod
    def set_sequence(description: str, stop: int, only_positive: bool = False) -> []:
        print(f'{description} : ', end='')
        values = []
        while True:
            try:
                value = int(input(
                    f'{values} : ' if len(values) > 0
                    else ""
                ))
                if only_positive:
                    if value < 0:
                        print(f'Введенное число должно быть больше 0!')
                        continue
                if value == stop:
                    if len(values) == 0:
                        print(f'Последовательность не содержит значений! Введите значение : ', end='')
                        continue
                    else:
                        return values
                values.append(value)
            except:
                print('Введенное значение не является вещественным числом, повторите!')
                continue

    @staticmethod
    def float_to_str(f):
        float_string = repr(f)
        if 'e' in float_string:  # detect scientific notation
            digits, exp = float_string.split('e')
            digits = digits.replace('.', '').replace('-', '')
            exp = int(exp)
            zero_padding = '0' * (abs(int(exp)) - 1)  # minus 1 for decimal point in the sci notation
            sign = '-' if f < 0 else ''
            if exp > 0:
                float_string = '{}{}{}.0'.format(sign, digits, zero_padding)
            else:
                float_string = '{}0.{}{}'.format(sign, zero_padding, digits)
        return float_string
