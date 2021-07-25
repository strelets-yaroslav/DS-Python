__author__ = "Yaroslav Strelets"

import helper


'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и
возвращает сумму наибольших двух аргументов.
'''

helper.print_task_description(3)


def sum_max_numbers(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 - min(num_1, num_2, num_3)


def sum_max_numbers_2(num_1, num_2, num_3):
    return sum(sorted((num_1, num_2, num_3))[1:])


number_1 = helper.get_number("Enter first number", float)
number_2 = helper.get_number("Enter second number", float)
number_3 = helper.get_number("Enter third number", float)

print(f"Sum of two max numbers from {number_1}, {number_2}, {number_3} is "
      f"{sum_max_numbers(number_1, number_2, number_3)}")
print(f"Sum of two max numbers from {number_1}, {number_2}, {number_3} by sorted tuple is "
      f"{sum_max_numbers(number_1, number_2, number_3)}")
