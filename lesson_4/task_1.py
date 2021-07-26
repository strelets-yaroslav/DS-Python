__author__ = "Yaroslav Strelets"

import os
from sys import argv, path
# import module from parent directory based on absolute path to the current script with __file__ (equals to argv[0])
path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
import helper as hlp

'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
время выполнения расчёта для конкретных значений необходимо запускать скрипт с
параметрами.
'''

if len(argv) != 4:
    print("Use script with 3 parameters (each is the float type!): [hours_worked] [rate_per_hour] [premium]\n"
          "Result of script will be Help or Salary value based on your three parameters.")
else:
    script_name, hours_worked, rate_per_hour, premium = argv
    hlp.print_task_description(1)
    try:
        print(f"Salary is {float(hours_worked) * float(rate_per_hour) + float(premium)}.")
    except ValueError:
        hlp.print_incorrect()
