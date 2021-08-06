__author__ = "Yaroslav Strelets"

import helper

'''
3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() вернет строку: *****\n*****\n*****.
'''


class Cell:
    __size = 0

    def __init__(self, size):
        try:
            self.__size = int(size)
            if self.__size <= 0:
                raise Exception("Wrong cell size: must be greater than 0!")
        except ValueError:
            raise Exception("Wrong cell size: must be numerical!")

    @property
    def size(self):
        return self.__size

    def __le__(self, other):
        return self.size <= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        if self <= other:
            return "The first cell is not greater than the second! Subtraction cannot be performed!"
        return Cell(self.size - other.size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def __truediv__(self, other):
        if self < other:
            return "The first cell is smaller than the second! Division cannot be performed!"
        return Cell(self.size // other.size)

    def make_order(self, row_size):
        return "\n".join(["*"*(min(row_size, self.size - i * row_size)) for i in range(1 + self.size // row_size)])


helper.print_task_description(3)

cell = Cell(17)
print("First cell order:")
print(cell.make_order(6))
cell_2 = Cell(9)
print("Second cell order:")
print(cell_2.make_order(4))

cell_sum = cell + cell_2
print(f"Sum cell and cell_2:\nSize = {cell_sum.size}, order:\n{cell_sum.make_order(10)}")
print(f"Difference cell and cell_2:\n{(cell - cell_2).make_order(3)}")
print(f"Incorrect subtraction example cell_2 - cell:\n{cell_2 - cell}")
cell_mul = cell * cell_2
print(f"Product of cell and cell_2, size: {cell_mul.size}")
print(f"Order (by 34):\n{cell_mul.make_order(34)}")
cell_div = cell / cell_2
print(f"Division cell by cell_2:\n{cell_div.make_order(2)}")

cell_3 = Cell(9)
print("Third cell order:")
print(cell_2.make_order(5))
cell_div_2 = cell / cell_3
print(f"Division cell by cell_3:\n{cell_div_2.make_order(2)}")
print(f"Incorrect division (cell / cell_2) / cell_3:\n{cell_div / cell_3}")
