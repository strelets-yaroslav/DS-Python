__author__ = "Yaroslav Strelets"

from time import sleep
import helper

'''
1. Создать класс TrafficLight (светофор).
● определить у него один атрибут color (цвет) и метод running (запуск);
● атрибут реализовать как приватный;
● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
зелёный;
● продолжительность первого состояния (красный) составляет 7 секунд, второго
(жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
● переключение между режимами должно осуществляться только в указанном порядке
(красный, жёлтый, зелёный);
● проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
выводить соответствующее сообщение и завершать скрипт.
'''


class TrafficLight:
    __color = ''

    def running(self, new_color):
        states = {
            'red': ('yellow', 7),
            'yellow': ('green', 2),
            'green': ('red', 5)
        }
        if (self.__color == '' and new_color not in states.keys()) or \
                (self.__color != '' and states.get(self.__color)[0] != new_color):
            print('Incorrect color! Exiting...')
            exit()

        print(f"Semaphore is set now to the '{new_color}' color..")
        self.__color = new_color
        sleep(states.get(self.__color)[1])


helper.print_task_description(1)

semaphore = TrafficLight()
# semaphore.running('blue')  # first running with incorrect color will exit
semaphore.running('yellow')
semaphore.running('green')
semaphore.running('red')
semaphore.running('yellow')
semaphore.running('red')  # running will be terminated here due to using the wrong color for the next semaphore state
semaphore.running('yellow')  # so this code will never run
