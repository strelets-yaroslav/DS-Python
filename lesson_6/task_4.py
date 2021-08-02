__author__ = "Yaroslav Strelets"

import helper

'''
4. Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.
'''


class Car:
    __is_police = False

    def __init__(self, name, color, speed=0):
        self.name = name
        self.color = color
        self.speed = speed

    def go(self, speed):
        msg = 'started the moving' if self.speed == 0 else 'changed the speed'
        self.speed = speed
        print(f"{self.color} {self.name} {msg}.")

    def stop(self):
        self.speed = 0
        print(f"{self.color} {self.name} stopped.")

    def turn(self, direction):
        print(f"{self.color} {self.name} turned to the {direction}.")

    def show_speed(self):
        print(f"{self.color} {self.name}'s current speed is {self.speed}.")

    def set_is_police(self):
        self.__is_police = True

    def check_is_police(self):
        msg = '' if self.__is_police else 'not '
        print(f'{self.name} is {msg}police car.')


class SportCar(Car):
    def __init__(self, color, speed=0):
        super().__init__('Porsche', color, speed)


class PoliceCar(Car):
    def __init__(self, name, color, speed=0):
        super().__init__(name, color, speed)
        self.set_is_police()


class TownCar(Car):
    def show_speed(self):
        max_speed = 60
        msg = f' It must slow down to {max_speed} m/h!' if self.speed > max_speed else ''
        print(f"{self.color} {self.name}'s current speed is {self.speed}.{msg}")


class WorkCar(Car):
    def show_speed(self):
        max_speed = 40
        msg = f' It must slow down to {max_speed} m/h!' if self.speed > max_speed else ''
        print(f"{self.color} {self.name}'s current speed is {self.speed}.{msg}")


helper.print_task_description(4)

sport_car = SportCar('red', 30)
kamaz = WorkCar('Kamaz', 'grey')
camry = TownCar('Camry', 'white')
ford = PoliceCar('Ford Focus', 'blue')

print(camry.color)
print(ford.color)
camry.check_is_police()
ford.check_is_police()
kamaz.check_is_police()
sport_car.go(90)
kamaz.go(50)
ford.show_speed()
ford.go(70)
sport_car.turn('left')
camry.go(50)
kamaz.show_speed()
ford.turn('right')
sport_car.show_speed()
sport_car.stop()
camry.show_speed()
camry.go(61)
camry.show_speed()
ford.stop()

sport_car.name = 'Maserati'
sport_car.color = 'black'
sport_car.go(150)
