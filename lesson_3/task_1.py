__author__ = "Yaroslav Strelets"

import helper


'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль.
'''

helper.print_task_description(1)


def my_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Division by zero!"


number_1 = helper.get_number("Enter first number", float)
number_2 = helper.get_number("Enter second number", float)

print(f"Result of division {number_1} and {number_2} = {my_divide(number_1, number_2)}")
