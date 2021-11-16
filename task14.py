from helper import Helper


class Task14:

    __task_number = 14

    def __init__(self, task_ended_callback):
        self.task_ended_callback = task_ended_callback

    @property
    def task_number(self):
        return self.__class__.__task_number

    def start_task(self):
        helper = Helper()
        print(f'------------------------- Задача {self.task_number} -------------------------')
        print('Вычислить приближенно значение бесконечной суммы:'
              '\n1/1*3 + 1/2*4 + 1/3*5 + ... = 3/4')
        epc = helper.set_degree_of_accuracy('Введите степень точности')
        print('----------------------------------------------------------')
        self.__calculate(epc, helper)
        print('----------------------------------------------------------')
        self.task_ended_callback(self.task_number)

    @staticmethod
    def __calculate(epc: float, helper: Helper):
        exact_value = 3 / 4
        epc_str = helper.float_to_str(epc)
        count_symbols = len(epc_str.split(".")[1])
        n1 = 1
        n2 = 3
        total_sum = 0.0
        while True:
            a = 1 / (n1 * n2)
            if abs(a) < epc:
                break
            total_sum += a
            n1 += 1
            n2 += 1
        helper.show_degree_of_accuracy_result(exact_value, round(total_sum, count_symbols), epc_str)
