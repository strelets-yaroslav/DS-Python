__author__ = "Yaroslav Strelets"

from helper import *

'''
6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
элемента — номер товара и словарь с параметрами, то есть характеристиками товара:
название, цена, количество, единица измерения. Структуру нужно сформировать программно,
запросив все данные у пользователя.
Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
характеристика товара, например, название. Тогда значение — список
значений-характеристик, например, список названий товаров.
'''

print_task_description(6)

characteristics = []
while True:
    key = input('Enter new characteristic of product or "n" for completion of filling: ')
    if key == 'n':
        break
    if key not in characteristics:
        characteristics.append(key)

print(f"List of characteristics is {characteristics}")

finish_choice = ('N', 'n')
products = []
product_number = 1
while True:
    print(f"Enter product #{product_number} data:")
    current_product = {}
    for item in characteristics:
        value = input(f"Enter value of #{product_number} product's {item}: ")
        current_product.update({item: value})

    products.append((product_number, current_product))

    action = input("Would you like to continue of filling? [Y/n]: ")
    if action in finish_choice:
        break

    product_number += 1

print(products)

analytics = {}
analytics_2 = {}
analytics_3 = {}
analytics_4 = {}
# take list of characteristics from 1st product (it equals to created characteristics list from user input)
parameters = list(products[0][1].keys())
for item in parameters:
    values = []
    for (index, product) in products:
        if product[item] not in values:
            values.append(product[item])
    analytics.update({item: values})

    # using comprehension+set - but order will be changed
    analytics_2.update({item: list(set([product[item] for (index, product) in products]))})

    # order will be saved
    analytics_3.update({item: list(dict.fromkeys([product[item] for (index, product) in products]))})
    # analog of "values & for" logic using in-time creating set - by (add or True) in if-condition
    unique = set()  # will store unique values
    analytics_4.update({
        item: [p[item] for (i, p) in products if p[item] not in unique and (unique.add(p[item]) or True)]
    })

print(f"Analytics dictionary is: {analytics}")
print(f"Analytics_2 dictionary is: {analytics_2}")
print(f"Analytics_3 dictionary is: {analytics_3}")
print(f"Analytics_4 dictionary is: {analytics_4}")
