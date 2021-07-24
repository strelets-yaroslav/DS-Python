"""
This is the module 'helper' for python lessons

Author = Yaroslav Strelets
"""


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
