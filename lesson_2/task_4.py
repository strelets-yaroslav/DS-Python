__author__ = "Yaroslav Strelets"

from helper import *


'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое
слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только
первые 10 букв в слове.
'''

print_task_description(4)

user_string = input("Enter a few words separated by a space: ")
separated_words = user_string.split()
max_len = 10
for (index, word) in enumerate(separated_words):
    print(f"#{index+1}: {word if len(word) <= max_len else word[:max_len]}")
