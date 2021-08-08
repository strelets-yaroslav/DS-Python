__author__ = "Yaroslav Strelets"

from random import randint
import helper


'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
'''

helper.print_task_description(5)

filename = "task_5.txt"
with open(filename, "w+") as task5_file:
    task5_file.write(" ".join([str(randint(1, 50)) for i in range(30)]))

    # now we are reading the file
    task5_file.seek(0)
    print(f"Sum of numbers in file: {sum([int(num) for num in task5_file.read().split()])}")
