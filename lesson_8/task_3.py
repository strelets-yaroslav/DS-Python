__author__ = "Yaroslav Strelets"

import helper as hlp

'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
пользователя данные и заполнять список необходимо только числами. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа
элемента. Вносить его в список, только если введено число. Класс-исключение должен не
позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
'''


class MyException(Exception):
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return f"'{self.__value}' is not a number!"


def my_int(input_str):
    if not input_str.isdigit():
        raise MyException(number)
    return int(input_str)


hlp.print_task_description(3)

numbers = []
while True:
    number = input("Enter digital number or 'quit' for exit: ")

    if number == "quit":
        print(f"Result list of numbers: {numbers}")
        exit()

    try:
        numbers.append(my_int(number))
    except MyException as e:
        print(e)
    except Exception as exc:  # it looks like this exception should never be thrown, but let it be =)
        print(f'Another exception was caught...\n{exc}')
