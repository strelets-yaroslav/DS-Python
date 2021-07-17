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

# print_task_description(3)
#
# number = 0
# while True:
#     number = input('Enter some number from 1 to 9: ')
#     if len(number) == 1 and number.isdigit() and int(number) > 0:
#         break
#     print('Incorrect number...', end=' ')
#
# double_number = int(number*2)
# triple_number = int(number*3)
# number = int(number)
# # numbers_sum = number + double_number + triple_number
# numbers_sum = sum([number, double_number, triple_number])
# print(f'Sum of {number}, {double_number}, {triple_number} is {numbers_sum}')


'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''

print_task_description(4)

number = 0
while True:
    number = input("Enter some positive number: ")
    if number.isdigit():
        break
    print("Incorrect number...", end=' ')

max_digit = max(number)
print(f'Result of max function by string as list (alphabetically): {max_digit}')

max_digit = 0
for (i, digit) in enumerate(number):
    current_digit = int(digit)
    max_digit = max(current_digit, max_digit)
    if max_digit == 9:
        break

print(f'Result of iterations on string as list: {max_digit}')

number = int(number)
max_digit = 0
while number > 0:
    current_digit = number % 10
    max_digit = max(current_digit, max_digit)
    if max_digit == 9:
        break
    number = number // 10

print(f'Result of divisions in number: {max_digit}')
