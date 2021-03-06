__author__ = "Yaroslav Strelets"

from itertools import cycle, count
import helper

'''
6. Реализовать два небольших скрипта:
● итератор, генерирующий целые числа, начиная с указанного;
● итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
повторение элементов списка прекратится.
'''

helper.print_task_description(6)


def count_example(start_num, end_num):
    num_iter = count(start_num)
    for i in range(start_num, end_num + 1):
        print(next(num_iter))


def cycle_example(max_iter, my_list):
    list_iter = cycle(my_list)
    for i in range(max_iter):
        print(next(list_iter))


start_number = helper.get_number("Enter start number")
end_number = helper.get_number("Enter end number")
count_example(start_number, end_number)

max_iterations = helper.get_number("Enter maximum number of cycle steps", is_pos=True)
my_list = helper.get_numbers(None)
cycle_example(max_iterations, my_list)
