__author__ = "Yaroslav Strelets"

import helper

'''
3. Реализовать базовый класс Worker (работник).
● определить атрибуты: name, surname, position (должность), income (доход);
● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
● создать класс Position (должность) на базе класса Worker;
● в классе Position реализовать методы получения полного имени сотрудника
(get_full_name) и дохода с учётом премии (get_total_income);
● проверить работу примера на реальных данных: создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров.
'''


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}, {self.position}"

    def get_total_income(self):
        return f"Total income is {self._income['wage'] + self._income['bonus']}"


helper.print_task_description(3)

name_ex = input("Enter name: ")
surname_ex = input("Enter surname: ")
position_ex = input("Enter position: ")
wage_ex = helper.get_number("Enter wage value", is_pos=True)
bonus_ex = helper.get_number("Enter bonus value", is_pos=True)

position_1 = Position(name_ex, surname_ex, position_ex, wage_ex, bonus_ex)
position_2 = Position("Ivan", "Ivanov", "CEO", 500, 250)
position_2.position = "CIO"

print("first Position instance:")
print(position_1.get_full_name())
print(position_1.get_total_income())
print(position_1._income)

print("another Position instance:")
print(position_2.get_full_name())
print(position_2.get_total_income())
print(position_2._income)
