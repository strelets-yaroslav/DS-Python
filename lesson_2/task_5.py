__author__ = "Yaroslav Strelets"

from helper import *


'''
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который
не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге
существуют элементы с одинаковыми значениями, то новый элемент с тем же значением
должен разместиться после них.
'''

print_task_description(5)

my_list = []
while True:
    item = input('Enter item value of "Rate" list or press "n" for completion of filling: ')
    if item == 'n':
        break
    if not item.isdigit():
        print_incorrect()
        continue

    item = int(item)
    item_index = 0
    length = len(my_list)
    my_set = set(my_list)
    if item in my_set:  # improve productivity in case of large list
        item_index = length - list(reversed(my_list)).index(item)
    else:
        item_index = next((ind for ind, itm in enumerate(my_list) if itm < item), length)

    new_item = "to the end of list" if item_index == length \
        else f"before first item with '{my_list[item_index]}' value"
    print(f'Inserting item in Rate list {new_item}: by {item_index} index')
    my_list.insert(item_index, item)
    print(f'Current Rate list value is {my_list}')

print(f'Final Rate list is {my_list}')
