__author__ = "Yaroslav Strelets"

import helper


'''
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
подсчёт строк и слов в каждой строке.
'''

helper.print_task_description(2)

with open("task_2.txt", "r") as task2_file:
    rows = task2_file.readlines()
    row_words_counts = [len(row.split()) for row in rows]
    print(f"Content of file: {rows}")
    print(f"Rows count in file: {len(rows)}")
    print(f"Count of words in each row: {row_words_counts}")
