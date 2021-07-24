__author__ = "Yaroslav Strelets"

import re
import helper


'''
6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод
исходной строки, но каждое слово должно начинаться с заглавной буквы. Используйте
написанную ранее функцию int_func().
'''

helper.print_task_description(6)


def int_func(word):
    return word.title()


while True:
    user_string = input("Enter a word (latin, in lower case): ")
    if user_string.isalpha() and user_string.islower():
        break
    helper.print_incorrect()

print(f"Task #6.1: New word is {int_func(user_string)}")

while True:
    user_string = input("Enter a few words (latin, in lower case) separated by a space: ")
    if re.match('^[a-z ]+$', user_string):
        break
    helper.print_incorrect()

new_string = " ".join([int_func(word) for word in user_string.split()])
print(f"Task #6.2: New string is {new_string}")
