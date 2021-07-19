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


def get_number(prompt='Enter number', non_zero=False):
    user_number = 0
    while True:
        user_number = input(prompt + ': ')
        if user_number.isdigit():
            user_number = int(user_number)
            if not non_zero or (non_zero and user_number != 0):
                break
        print_incorrect()
    return user_number
