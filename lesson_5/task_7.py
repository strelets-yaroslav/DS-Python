__author__ = "Yaroslav Strelets"

import re, json
from statistics import mean
import helper

'''
7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
'''

helper.print_task_description(7)

firms_profit = [{}, {}]
with open("task_7.txt", "r", encoding="UTF-8") as task7_file:
    lines = [line.replace("\n", "") for line in task7_file.readlines()]
    for line in lines:
        firm = re.findall(r"^(.*) (.*?) (.*?) (.*?)$", line)[0]
        firms_profit[0].update({firm[0]: float(firm[2]) - float(firm[3])})
    firms_profit[1].update({"average_profit": mean([profit for profit in firms_profit[0].values() if profit > 0])})

print(firms_profit)

with open("task7.json", "w+", encoding="UTF-8") as task7_new_file:
    json.dump(firms_profit, task7_new_file)
    print("checking the result from json file...")
    task7_new_file.seek(0)
    print(json.load(task7_new_file))
