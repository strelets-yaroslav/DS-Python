__author__ = "Yaroslav Strelets"

import re
import helper


'''
6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по
нему. Вывести его на экран.
'''

helper.print_task_description(6)

lessons = {}
with open("task_6.txt", "r", encoding="UTF-8") as task6_file:
    lines = [line.replace("\n", "") for line in task6_file.readlines()]
    for line in lines:
        # could not define the regular expression option so just replace '-' with '0()'...
        row = re.findall(r"^(.*): (.*?)[(].* (.*?)[(].* (.*?)[(].*$", line.replace("-", "0()"))[0]
        lessons.update({row[0]: sum([int(num) for num in row[1:]])})

print(lessons)
