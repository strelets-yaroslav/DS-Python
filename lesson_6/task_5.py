__author__ = "Yaroslav Strelets"

import helper

'''
5. Реализовать класс Stationery (канцелярская принадлежность).
● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
сообщение «Запуск отрисовки»;
● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
● в каждом классе реализовать переопределение метода draw. Для каждого класса
метод должен выводить уникальное сообщение;
● создать экземпляры классов и проверить, что выведет описанный метод для каждого
экземпляра.
'''


class Stationery:
    title = 'Base'

    def draw(self):
        print(f"Start drawing...")


class Pen(Stationery):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} drawing...")


class Pencil(Stationery):
    def draw(self):
        print(f"Pencil drawing...")


class Handle(Stationery):
    def draw(self):
        print(f"{self.__class__.__name__} drawing...")


helper.print_task_description(5)

stationary = Stationery()
pen = Pen('Pen')
pencil = Pencil()
handle = Handle()
stationary.draw()
pen.draw()
pencil.draw()
handle.draw()
