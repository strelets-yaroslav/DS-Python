__author__ = "Yaroslav Strelets"

import helper


'''
4. Программа принимает действительное положительное число x и целое отрицательное число
y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с
помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
'''

helper.print_task_description(4)


def my_exponentiation_1(base, degree):
    return base ** degree


def my_exponentiation_2(base, degree):
    index = 1
    exp_result = 1.0 / base
    while index < abs(degree):
        exp_result /= base
        index += 1
    return exp_result


number = helper.get_number("Enter positive number", float, True)
user_degree = helper.get_number("Enter integer negative number", is_neg=True)

print(f"Pow result of {number} with {user_degree} degree is {pow(number, user_degree)}")
print(f"{number} in {user_degree} degree by ** is {my_exponentiation_1(number, user_degree)}")
print(f"{number} in {user_degree} degree by cycle is {my_exponentiation_2(number, user_degree)}")
