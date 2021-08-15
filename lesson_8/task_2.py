__author__ = "Yaroslav Strelets"

import helper as hlp

'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''


class MyDivisionByZero(Exception):
    def __init__(self):
        self.txt = 'Dividing by zero cannot be performed!'

    def __str__(self):
        return self.txt


hlp.print_task_description(2)

number_1 = hlp.get_number("Enter first number", float)
number_2 = hlp.get_number("Enter second number", float)

try:
    if number_2 == 0:
        raise MyDivisionByZero
    result = number_1 / number_2
except MyDivisionByZero as e:
    print(e)
else:
    print(result)
