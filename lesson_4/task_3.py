__author__ = "Yaroslav Strelets"

import helper

'''
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну
строку.
Подсказка: используйте функцию range() и генератор.
'''

helper.print_task_description(3)
min_num = 20
max_num = 240
first_mod = 20
second_mod = 21
result = [num for num in range(min_num, max_num + 1) if num % first_mod == 0 or num % second_mod == 0]
print(f"List of numbers in the range from {min_num} to {max_num} that are divisible by "
      f"{first_mod} or {second_mod} without remainder is\n{result}")
