__author__ = "Yaroslav Strelets"

import helper as hlp

'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
оргтехники на склад и передачу в определённое подразделение компании. Для хранения
данных о наименовании и количестве единиц оргтехники, а также других данных, можно
использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
пользователем данных. Например, для указания количества принтеров, отправленных на
склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''


class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @property
    def hash_str(self):
        return f'{self.brand}_{self.model}'

    @property
    def name(self):
        return f'{self.__class__.__name__}s'

    def __str__(self):
        return f'{self.brand} {self.model}'


class Printer(OfficeEquipment):
    def __init__(self, brand, model, colored):
        super(Printer, self).__init__(brand, model)
        self.colored = colored

    @property
    def hash_str(self):
        return f'{super(Printer, self).hash_str}_{self.colored}'

    def __str__(self):
        return f'{super(Printer, self).__str__()}, {self.colored}'


class Scanner(OfficeEquipment):
    pass


class DesktopComputer(OfficeEquipment):
    def __init__(self, brand, model, preinstalled_os=None):
        super(DesktopComputer, self).__init__(brand, model)
        self.preinstalled_os = preinstalled_os

    @property
    def hash_str(self):
        return f'{super(DesktopComputer, self).hash_str}_{self.preinstalled_os}'

    def __str__(self):
        return f'{super(DesktopComputer, self).__str__()}, OS: {self.preinstalled_os}'


class Warehouse:
    def __init__(self, name):
        self.__name = f'warehouse_{name}'
        self.__equipments = {self.__name: {}}

    @staticmethod
    def check_count(count):
        return type(count) == int and count > 0

    def buy_equipment(self, equipment, count):
        if not Warehouse.check_count(count):
            return "Wrong value of count! It must be positive number!"

        # did not use the list of class instances for the sake of less memory usage...

        equipment_name = equipment.name
        concrete_equipment = equipment.hash_str
        if equipment_name in self.__equipments[self.__name]:
            if concrete_equipment in self.__equipments[self.__name][equipment_name]:
                self.__equipments[self.__name][equipment_name][concrete_equipment] += count
            else:
                self.__equipments[self.__name][equipment_name].update({concrete_equipment: count})
        else:
            self.__equipments[self.__name].update({equipment_name: {concrete_equipment: count}})

        return f"Equipment {str(equipment)} was added!"

    def move_equipment(self, unit_name, equipment, count, concrete=False, backward=False):
        if not Warehouse.check_count(count):
            return "Wrong value of count! It must be positive number!"

        src = unit_name if backward else self.__name
        dst = self.__name if backward else unit_name

        if src == dst:
            return 'One unit used - nothing to move!'

        equipment_name = equipment.name
        equipment_concrete = equipment.hash_str

        if src not in self.__equipments:
            return f"Unit '{src}' does not have any equipments!"
        if equipment_name not in self.__equipments[src]:
            return f"Unit '{src}' has not {equipment_name} equipments!"
        if concrete and equipment_concrete not in self.__equipments[src][equipment_name]:
            return f"Unit '{src}' has not '{str(equipment)}' equipments!"

        if concrete:
            equipment_count = self.__equipments[src][equipment_name][equipment_concrete]
        else:
            equipment_count = sum(list(self.__equipments[src][equipment_name].values()))

        if equipment_count < count:
            return f"There are not necessary equipments to move - only {equipment_count} pieces."

        if dst not in self.__equipments:
            self.__equipments.update({dst: {equipment_name: {}}})

        if equipment_name not in self.__equipments[dst]:
            self.__equipments[dst].update({equipment_name: {}})

        if concrete:
            self.__equipments[src][equipment_name][equipment_concrete] -= count
            if equipment_concrete in self.__equipments[dst][equipment_name]:
                self.__equipments[dst][equipment_name][equipment_concrete] += count
            else:
                self.__equipments[dst][equipment_name].update({equipment_concrete: count})
        else:
            for model, model_count in list(self.__equipments[src][equipment_name].items()):
                if count < model_count:
                    self.__equipments[src][equipment_name][model] -= count
                    if model in self.__equipments[dst][equipment_name]:
                        self.__equipments[dst][equipment_name][model] += count
                    else:
                        self.__equipments[dst][equipment_name].update({model: count})
                else:
                    if model in self.__equipments[dst][equipment_name]:
                        self.__equipments[dst][equipment_name][model] += model_count
                    else:
                        self.__equipments[dst][equipment_name].update({model: model_count})
                    del(self.__equipments[src][equipment_name][model])

                count -= model_count
                if count <= 0:
                    break

            if len(self.__equipments[src][equipment_name]) == 0:
                del(self.__equipments[src][equipment_name])
                if len(self.__equipments[src]) == 0:
                    del(self.__equipments[src])

        return f"Equipment {str(equipment)} was moved!"

    @property
    def total_count(self):
        equipment_count = 0
        for unit in self.__equipments.values():
            equipment_count += sum([sum(list(equipment.values())) for equipment in unit.values()])
        return equipment_count

    @property
    def equipments_count(self):
        result_dict = {}
        for unit in self.__equipments.values():
            for eq_name, eq in unit.items():
                equipment_count = 0
                for model in eq.values():
                    equipment_count += model

                if eq_name in result_dict:
                    result_dict[eq_name] += equipment_count
                else:
                    result_dict.update({eq_name: equipment_count})

        return result_dict

    def __str__(self):
        result_str = ''
        sep = ' '
        for unit_name, unit in self.__equipments.items():
            result_str += f'In {unit_name if unit_name != self.__name else "Warehouse"}:\n'
            for eq_name, eq in unit.items():
                result_str += f'{sep:>5}{eq_name}:\n'
                for model_hash, count in eq.items():
                    model = model_hash.split('_')
                    model = f'{model[0]}, {model[1]}{", " + model[2] if len(model) == 3 else ""}'
                    result_str += f'{sep:>10}{model}: {count}\n'
        return result_str


hlp.print_task_description(7)

warehouse_1 = Warehouse('1')
printer_1 = Printer('HP', 'LaserJet M1200', 'w/b')
print(warehouse_1.buy_equipment(printer_1, 5))
printer_2 = Printer('HP', 'LaserJet P1000', 'c')
print(warehouse_1.buy_equipment(printer_2, 3))
print(warehouse_1.buy_equipment(printer_1, 2))

scanner_1 = Scanner('HP', 'M500')
warehouse_1.buy_equipment(scanner_1, 10)

computer_1 = DesktopComputer('Apple', 'MacBook', 'Mac Tiger')
computer_2 = DesktopComputer('Apple', 'MacBook', 'Mac 10')
warehouse_1.buy_equipment(computer_1, 12)
warehouse_1.buy_equipment(computer_2, 4)

# wrong count value
print(warehouse_1.buy_equipment(computer_2, '4'))

print(f'Total equipment count: {warehouse_1.total_count}')
print(warehouse_1.equipments_count)
print(warehouse_1)
print(warehouse_1.move_equipment('Buh', computer_2, 3, concrete=True))
print(warehouse_1)
print(warehouse_1.move_equipment('Sales', printer_1, 8))

print(warehouse_1)

# has not equipments
print(warehouse_1.move_equipment('Buh', printer_1, 2, backward=True))
# has not enough equipments
print(warehouse_1.move_equipment('Buh', computer_1, 5, backward=True))
# not enough models
print(warehouse_1.move_equipment('Sales', printer_2, 4, concrete=True))

print(warehouse_1.move_equipment('Sales', printer_1, 3, backward=True))
print(warehouse_1)

print(warehouse_1.move_equipment('Buh', computer_1, 3, backward=True))
print(warehouse_1)
print(f'Total equipment count: {warehouse_1.total_count}')
print(warehouse_1.equipments_count)
