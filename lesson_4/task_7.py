__author__ = "Yaroslav Strelets"

from math import factorial as mfact
import helper

'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное
значение. При вызове функции должен создаваться объект-генератор. Функция вызывается
следующим образом: for el in fact(n). Она отвечает за получение факториала числа. В цикле
нужно выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисе.л от 1 до n Например, факториал
четырёх 4! = 1 * 2 * 3 * 4 = 24.
'''

helper.print_task_description(7)


def fact(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
        yield f


max_number = helper.get_number("Enter max number fo factorials")
for number, factorial in enumerate(fact(max_number), 1):
    print(f"Factorial of {number} is {factorial}")

for number in range(1, max_number + 1):
    print(f"Factorial with math of {number} is {mfact(number)}")
