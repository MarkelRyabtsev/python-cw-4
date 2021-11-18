import random


class Helper:

    @staticmethod
    def set_natural_number(description: str, numbers_range: range = None, all_numbers: bool = False) -> int:
        while True:
            try:
                value = int(input(f'{description} : '))
                if not all_numbers:
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
            for i in range(0, len(row)):
                str_value = str(row[i])
                if len(str_value) == 1:
                    str_value = f'  {str_value}'
                elif len(str_value) == 2:
                    str_value = f' {str_value}'
                print(f'[{str_value}]', end='')
            print('')

    @staticmethod
    def print_long_array(array: []):
        count = 1
        print('[', end='')
        for element in array:
            if count == len(array):
                print(f'{element}', end='')
            elif count % 15 != 0:
                print(f'{element}, ', end='')
            else:
                print(f'{element},')
            count += 1
        print(']')

    @staticmethod
    def swap_items(a: int, b: int):
        temp = a
        a = b
        b = temp
        return a, b

