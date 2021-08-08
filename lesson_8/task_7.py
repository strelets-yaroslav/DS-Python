__author__ = "Yaroslav Strelets"

import helper as hlp

'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
'''


class MyComplex:
    __a = 0
    __b = 0

    def __init__(self, real_part, imaginary_part):
        self.__a = real_part
        self.__b = imaginary_part

    def __str__(self):
        return f"{self.__a} + {self.__b}i"

    def __add__(self, other):
        return MyComplex(self.__a + other.__a, self.__b + other.__b)

    def __mul__(self, other):
        a = self.__a * other.__a - self.__b * other.__b
        b = self.__b * other.__a + self.__a * other.__b
        return MyComplex(a, b)


hlp.print_task_description(7)
my_complex_1 = MyComplex(2, 3)
print(my_complex_1)

my_complex_2 = MyComplex(1, 5)
print(my_complex_2)

my_complex_3 = MyComplex(-2, 8)
print(my_complex_3)

print(f"sum 1st and 2nd: {my_complex_1 + my_complex_2}")
print(f"multiply 1st and 2nd: {my_complex_1 * my_complex_2}")
print(f"sum 1st and 3rd: {my_complex_1 + my_complex_3}")
print(f"multiply 2nd and 3rd: {my_complex_2 * my_complex_3}")
