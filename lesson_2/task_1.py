__author__ = "Yaroslav Strelets"

from helper import *


'''
1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
'''

print_task_description(1)

my_list = [3, [4, "rrt"], "test", 5.44, None, {"1": 23, "2": "test2"}]
my_list.insert(3, True)
my_list.remove("test")
my_list.append("new element")
my_list.extend([1, ('m', 'o', 'r', 'e'), 0])
print(my_list)

for item in my_list:
    print(type(item))
