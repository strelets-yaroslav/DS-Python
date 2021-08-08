__author__ = "Yaroslav Strelets"

from re import match
import helper as hlp

'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
реальных данных.
'''


class MyDate:
    __months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    __postfix_tuple = ('th', 'st', 'nd', 'rd')

    def __init__(self, date_str):
        self.__value = MyDate.parse_date(date_str)

    @staticmethod
    def check_date_values(day, month, year):
        days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if month < 1 or month > 12:
            return 'Wrong month! It must be from 1 to 12!'
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days[2] = 29
        if day > days[month] or day < 1:
            return f'Wrong day! It must be from 1 to {days[month]}!'

        return 'OK'

    @classmethod
    def parse_date(cls, date_str):

        if not match(r"^[\d]{1,2}-[\d]{1,2}-[\d]{1,4}$", date_str):
            return "Incorrect date! It must be in 'day-month-year' format with integer values!"

        (day, month, year) = [int(value) for value in date_str.split("-")]
        date = MyDate.check_date_values(day, month, year)
        if date == 'OK':
            last_digit = day % 10
            tenth = day // 10
            postfix = cls.__postfix_tuple[0 if last_digit > 3 or tenth == 1 else last_digit]
            return f"Date: {cls.__months[month]} {day}{postfix}, {year}."
        else:
            return date

    def __str__(self):
        return f"{self.__value}"


hlp.print_task_description(1)

print(MyDate.check_date_values(3, 13, 2004))
print(MyDate.check_date_values(30, 3, 100))

my_date = MyDate("1-10-2000")
print(my_date)

print(MyDate("03-10-200O"))  # 'O' instead of '0' in the last year's symbol

print(MyDate("29-02-1900"))
print(MyDate("28-02-2004"))
print(MyDate("12-12-2012"))
print(MyDate("22-5-2021"))
