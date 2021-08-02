__author__ = "Yaroslav Strelets"

import re
import helper


'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
этом английские числительные должны заменяться на русские. Новый блок строк должен
записываться в новый текстовый файл.
'''

helper.print_task_description(4)

dict_numerals = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_lines = []
with open("task_4.txt", "r") as task4_file:
    lines = [line.replace("\n", "") for line in task4_file.readlines()]
    for line in lines:
        row = re.split(' - ', line)
        new_lines.append(f"{dict_numerals.get(row[0])} - {row[1]}\n")

with open("task_4_new.txt", "w", encoding='UTF-8') as task4_file:
    task4_file.writelines(new_lines)
    print("Completed new file 'task_4_new.txt'.")
