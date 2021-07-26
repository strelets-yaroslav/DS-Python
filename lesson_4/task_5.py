__author__ = "Yaroslav Strelets"

from functools import reduce
import helper

'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В
список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

helper.print_task_description(5)


def multiply_elements(prev_el, el):
    return prev_el * el


start = 100
end = 1000
mod_num = 2
mod_cond = 0
result = reduce(multiply_elements, [num for num in range(start, end + 1) if num % mod_num == mod_cond])
print(f"Multiply of numbers in the range from {start} to {end} including {end} that are divisible by "
      f"{mod_num} with {mod_cond} remainder is\n{result}")

mult = 1
for num in range(start, end + 1):
    if num % mod_num == mod_cond:
        mult *= num
print(f"Just to test this result by multiplying in the loop:\n{mult}")
