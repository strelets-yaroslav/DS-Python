"""
This is the module 'helper' for python lessons

Author = Yaroslav Strelets
"""

import re


def print_task_description(task_number):
    sep = '-' * 80
    task_description = f'Task #{task_number}'
    print(f'{sep}')
    print(f'{task_description:^80}')
    print(f'{sep}')


def print_incorrect():
    print('Incorrect value...', end=' ')


def get_number(prompt='Enter number', number_type=int, is_pos=False, is_neg=False, non_zero=False):
    """
    takes user input and tries to convert it to the type pointed to by the number_type parameter,
    additionally checking several possible conditions.

    :param prompt: prompt for user input (default - 'Enter number') - str
    :param number_type: type for number (default - int) - type
    :param is_pos: is number positive (default - False) - boolean
    :param is_neg: is number negative (default - False) - boolean
    :param non_zero: is number not equal zero (default - False) - boolean
    :return: number - type of number_type param
    """
    while True:
        user_number = input(prompt + ': ')
        try:
            user_number = number_type(user_number)
        except ValueError:
            pass
        else:
            if not (is_neg or is_pos or non_zero):
                break

            if is_pos and user_number > 0:
                break

            if is_neg and user_number < 0:
                break

            if non_zero and user_number != 0:
                break

        print_incorrect()
    return user_number


def get_numbers(number_type=int):
    """
    takes user input as string of numbers separated by a space and tries to convert each of them to 'number_type' type

    :param number_type: type for number's converting (to [int (default) | float | str | bool] only)
    :return: list of numbers
    """

    regulars = {
        str: ('^.*$', 'symbols'),
        int: ('^[0-9 ]+$', 'int numbers'),
        float: ('^[0-9. ]+$', 'float numbers'),
        bool: ('^(False|True| )+$', 'booleans')
    }

    while True:
        if number_type not in regulars.keys():
            number_type = str
        numbers = input(f'Enter list of {regulars[number_type][1]} separated by a space: ')
        if re.match(regulars[number_type][0], numbers):
            my_list = [number_type(number) for number in numbers.split()]
            break
        print_incorrect()
    return my_list
