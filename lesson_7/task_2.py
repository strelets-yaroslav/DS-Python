__author__ = "Yaroslav Strelets"

from abc import ABC, abstractmethod
import helper

'''
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
'''


class Clothes(ABC):
    @abstractmethod
    def calc_fabric(self):
        pass


class Coat(Clothes):
    __size = 0

    def __init__(self, size):
        self.__size = float(size)

    @property
    def calc_fabric(self):
        return self.__size * 6.5 + 0.5


class Suit(Clothes):
    __height = 0

    def __init__(self, height):
        self.__height = float(height)

    @property
    def calc_fabric(self):
        return self.__height * 2 + 0.3


class Studio:
    __coats = []
    __suits = []

    def add_coats(self, sizes):
        self.__coats = [Coat(size) for size in sizes]

    def add_suits(self, heights):
        self.__suits = [Suit(height) for height in heights]

    @property
    def calc_total_fabric(self):
        coats_fabric = sum([coat.calc_fabric for coat in self.__coats]) if len(self.__coats) > 0 else 0
        suits_fabric = sum([suit.calc_fabric for suit in self.__suits]) if len(self.__suits) > 0 else 0
        return coats_fabric + suits_fabric


helper.print_task_description(2)

studio_1 = Studio()
studio_1.add_coats([50, 48.5, 51.5])
studio_1.add_suits([175, 180, 185, 190])
print(f"Total fabric consumption of the first studio: {studio_1.calc_total_fabric}")

studio_2 = Studio()
studio_2.add_coats([56.5, 56.5, 57])
studio_2.add_suits([155, 168, 160, 160, 175])
print(f"Total fabric consumption of the second studio: {studio_2.calc_total_fabric}")

studio_3 = Studio()
studio_3.add_suits([])
studio_3.add_coats([45, 46, 47])
print(f"Total fabric consumption of the third studio: {studio_3.calc_total_fabric}")
