__author__ = "Yaroslav Strelets"

import helper

'''
2. Реализовать класс Road (дорога).
● определить атрибуты: length (длина), width (ширина);
● значения атрибутов должны передаваться при создании экземпляра класса;
● атрибуты сделать защищёнными;
● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
дороги асфальтом, толщиной в 1 см*число см толщины полотна;
● проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''


class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self, asphalt_mass, roadway_thickness):
        mass = self._length * self._width * asphalt_mass * roadway_thickness
        return f'{round(mass / 1000)} tonnes'


helper.print_task_description(2)

length = helper.get_number("Enter road length value", is_pos=True)
width = helper.get_number("Enter road width value", is_pos=True)
mass = helper.get_number("Enter mass of asphalt in sq.m/sm", is_pos=True)
thick = helper.get_number("Enter roadway thickness", is_pos=True)

road = Road(length, width)
print(f"Asphalt mass for the road will be {road.calc(mass, thick)}")
