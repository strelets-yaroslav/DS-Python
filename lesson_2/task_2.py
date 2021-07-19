__author__ = "Yaroslav Strelets"

from helper import *


'''
2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
input().
'''

print_task_description(2)

my_list = []
while True:
    item = input('Enter new item or press "n" for completion of filling: ')
    if item == 'n':
        break
    my_list.append(item)

print(f"Started list is {my_list}")

index = 0
# while (index + 1) < len(my_list):
for i in range(len(my_list)//2):
    my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]
    index += 2

print(f"Updated list is {my_list}")
