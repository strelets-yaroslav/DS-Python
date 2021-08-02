__author__ = "Yaroslav Strelets"

import helper

'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения
которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его
формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''

helper.print_task_description(2)

my_list = helper.get_numbers()
print(f"Started list is {my_list}")
print(f"Finish list is {[my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]}")
