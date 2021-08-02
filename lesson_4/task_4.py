__author__ = "Yaroslav Strelets"

from random import randint
import helper

'''
4. Представлен список чисел. Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в
порядке их следования в исходном списке. Для выполнения задания обязательно используйте
генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''

helper.print_task_description(4)

my_list = [randint(1, 20) for i in range(25)]
print(f"Started list is {my_list}")
print(f"Finish list is {[num for num in my_list if my_list.count(num) == 1]}")
