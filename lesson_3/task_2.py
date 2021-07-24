__author__ = "Yaroslav Strelets"

import helper

'''
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные
пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
должна принимать параметры как именованные аргументы. Осуществить вывод данных о
пользователе одной строкой.
'''

helper.print_task_description(2)


def print_user_data(name, surname, year, city, email, phone):
    return f"User: {surname} {name}, born in {year}, lives in {city} city. Contacts: email: {email}, phone: {phone}"


print("Enter user data:")
user_name = input("name: ")
user_surname = input("surname: ")
birth_year = input("birth year: ")
user_city = input("city: ")
user_email = input("email: ")
user_phone = input("phone: ")

print(print_user_data(name=user_name, surname=user_surname, year=birth_year, city=user_city,
                      email=user_email, phone=user_phone))
