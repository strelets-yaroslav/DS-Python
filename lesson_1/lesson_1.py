__author__ = "Yaroslav Strelets"


def print_task_description(task_number):
    sep = '-' * 80
    task_description = f'Task #{task_number}'
    print(f'{sep}')
    print(f'{task_description:^80}')
    print(f'{sep}')


'''
1. Поработайте с переменными, создайте несколько, выведите на экран. Запросите у
пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
'''

# print_task_description(1)
#
# first_var = "I'm first var"
# second_var = 3
# third_var = [1, 2, 'fff']
# print(f"first vars: string - {first_var}; number - {second_var}; list - {third_var}")
#
# user_first_var = input('Enter some var: ')
# user_second_var = input('And a bit more...: ')
# print(f'You entered: {user_first_var} and {user_second_var}')


'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и
выведите в формате чч:мм:сс. Используйте форматирование строк.
'''

# print_task_description(2)
#
# raw_seconds = 0
# while True:
#     raw_seconds = input('Enter time in seconds: ')
#     if raw_seconds.isdigit():
#         raw_seconds = int(raw_seconds)
#         break
#     print('Digit is required...', end=' ')
#
# seconds = raw_seconds % 60
# minutes = (raw_seconds % 3600) // 60
# raw_hours = raw_seconds // 3600
# print(f'{raw_hours:02d}:{minutes:02d}:{seconds:02d}')
# if raw_hours > 23:
#     hours = raw_hours % 24
#     days = raw_hours // 24
#     print(f'{days} days {hours:02d}:{minutes:02d}:{seconds:02d}')


'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

print_task_description(3)

number = 0
while True:
    number = input('Enter some number from 1 to 9: ')
    if len(number) == 1 and number.isdigit() and int(number) > 0:
        break
    print('Incorrect number...', end=' ')

double_number = int(number*2)
triple_number = int(number*3)
number = int(number)
# numbers_sum = number + double_number + triple_number
numbers_sum = sum([number, double_number, triple_number])
print(f'Sum of {number}, {double_number}, {triple_number} is {numbers_sum}')
