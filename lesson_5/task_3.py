__author__ = "Yaroslav Strelets"

import re
import helper


'''
3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
сотрудников.
'''

helper.print_task_description(3)

salaries = {}
with open("task_3.txt", "r") as task3_file:
    lines = [line.replace("\n", "") for line in task3_file.readlines()]
    for line in lines:
        try:
            line_tuple = re.findall(r"^(.*) (.*)$", line)[0]
            salaries.update({line_tuple[0]: float(line_tuple[1])})
        except Exception:
            pass

print(salaries)
print(f"People who have salary less than 20000: {[name for name, salary in salaries.items() if salary < 20000]}")
print(f"Average salary: {round(sum(salaries.values()) / len(salaries), 2)}")
