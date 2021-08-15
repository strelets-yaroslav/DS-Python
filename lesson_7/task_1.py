__author__ = "Yaroslav Strelets"

from random import randint
import helper

'''
1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''


class MatrixRow:
    __values = []
    __len = 0
    __number_width = 5

    def __init__(self, values):
        try:
            self.__values = [round(float(values[i]), 2) for i in range(len(values))]
        except ValueError:
            raise Exception("Cannot create an instance of Matrix class row coz of 'values' has incorrect structure:\n"
                            "It should contains list of numeric values!")
        self.__len = len(values)

    @property
    def len(self):
        return self.__len

    @property
    def width(self):
        return self.__number_width

    @width.setter
    def width(self, number_width):
        self.__number_width = number_width

    def __getitem__(self, item):
        if 0 <= item < self.len:
            return self.__values[item]
        else:
            return None

    def __str__(self):
        return f"  ".join([str(self[i]).ljust(self.width) for i in range(self.len)])

    def __add__(self, other):  # for now it does not use coz of get matrix item by indices
        return MatrixRow([(self[i] + other[i]) for i in range(self.len)])


class Matrix:
    __values = []
    __width = 0
    __height = 0

    def __init__(self, values):
        check_values = [len(values[i]) != len(values[i - 1]) for i in range(1, len(values))]
        if any(check_values):
            raise Exception("Cannot create an instance of Matrix class coz of 'values' has incorrect structure:\n"
                            "It should contains lists with the same length!")

        self.__values = [MatrixRow(values[i]) for i in range(len(values))]
        self.__height = len(self.__values)
        self.__width = self.__values[0].len
        max_number_width = max([max(len(str(self[i][j])) for i in range(self.__height) for j in range(self.__width))])
        for row in self.__values:
            row.width = max_number_width

    def __getitem__(self, item):
        if 0 <= item < self.__height:
            return self.__values[item]
        else:
            return None

    def __str__(self):
        return "\n".join([str(row) for row in self.__values])

    def __ne__(self, other):
        return self.__width != other.__width or self.__height != other.__height

    def __add__(self, other):
        if self != other:
            return "Matrices are not the same size!"
        # values = [(row1 + row2) for row1 in self.__values for row2 in other.__values]
        values = [[self[i][j] + other[i][j] for j in range(self.__width)] for i in range(self.__height)]
        return Matrix(values)


helper.print_task_description(1)

a = Matrix([[1, 2, -5, 10], [3, -4, 2.5, 500], [18, -2, 45.66, 71]])
print(f"First matrix is:\n{a}")
b = Matrix([[11, -52, 8, -3.6], [4, -104.21, 0.6, -21], [-1, 0, 1, 1]])
print(f"Second matrix is:\n{b}")
matrix_sum = a + b
print(f"New matrix is:\n{matrix_sum}")

c = Matrix([[1, 2, 3, 3], [4, 5, 6, 7]])
print(f"Third matrix is:\n{c}")
print(f"Sum of first and third matrices:\n{a + c}")

rand_values = [[round(randint(-2500, 2500)/1.1, 2) for j in range(4)] for i in range(3)]
d = Matrix(rand_values)
print(f"Fourth matrix is:\n{d}")
matrix_sum_2 = d + matrix_sum
print(f"Sum of first and previous matrix sum:\n{matrix_sum_2}")

print(f"Element of the last matrix sum in second row and third column cell is {matrix_sum_2[1][2]}")

error_matrix_init = Matrix([[1, 2], [3, 4, 5], [6, 7]])  # incorrect structure - the exception will be raised here!
