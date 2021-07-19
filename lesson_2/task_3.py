__author__ = "Yaroslav Strelets"

from helper import *


'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.
'''

print_task_description(3)

season_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer",
               "autumn", "autumn", "autumn", "winter"]
season_dict_1 = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer",
                 7: "summer", 8: "summer", 9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
season_dict_2 = {"winter": (1, 2, 12), "spring": (3, 4, 5), "summer": (6, 7, 8), "autumn": (9, 10, 11)}
season_dict_3 = {(1, 2, 12): "winter", (3, 4, 5): "spring", (6, 7, 8): "summer", (9, 10, 11): "autumn"}

month = 0
while True:
    month = input("Enter numeric value of month (1 - 12): ")
    if not month.isdigit():
        print_incorrect()
    else:
        month = int(month)
        if 13 > month > 0:
            break
        print_incorrect()

season = ''
for (key, values) in season_dict_2.items():
    if month in values:
        season = key
        break

seasons = list(season_dict_2.keys())
months = sum(list(season_dict_2.values()), ())
season_2 = seasons[months.index(month) // 3]

season_3 = [season for (season, val) in season_dict_2.items() if month in val][0]
season_4 = [season for (key, season) in season_dict_3.items() if month in key][0]
season_5 = next((season for (season, val) in season_dict_2.items() if month in val))
season_6 = next((season for (key, season) in season_dict_3.items() if month in key))

print(f'Season by list for {month} is {season_list[month-1]}')
print(f'Season by dict (number: season) for {month} is {season_dict_1.get(month)}')
print(f'Season by dict (season: (months)) by "for in" for {month} is {season}')
print(f'Season by dict (season: (months)) by keys/values lists for {month} is {season_2}')
print(f'Season by dict (season: (months)) by comprehension for {month} is {season_3}')
print(f'Season by dict ((months): season) by comprehension for {month} is {season_4}')
print(f'Season by dict (season: (months)) by next+comprehension for {month} is {season_5}')
print(f'Season by dict ((months): season) by next+comprehension for {month} is {season_6}')
