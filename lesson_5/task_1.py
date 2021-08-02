__author__ = "Yaroslav Strelets"

import helper


'''
1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
строка.
'''

helper.print_task_description(1)

prompt = "Enter some text for the file saving: "
with open("task_1.txt", "w") as task1_file:
    text = input(prompt)
    while text:
        task1_file.write(text + "\n")
        text = input(prompt)
