__author__ = "Yaroslav Strelets"

import helper


'''
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом. При нажатии
Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет
добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму
этих чисел к полученной ранее сумме и после этого завершить программу.
'''

helper.print_task_description(5)


def print_my_sum(accumulated_sum):
    print(f"Accumulated sum now is {accumulated_sum}")


def my_sum(accumulated_sum=0):
    current_numbers = input("Enter a few numbers separated by a space. For exit enter symbol 'q'. ")
    for current_number in current_numbers.split():
        if current_number == "q":
            print_my_sum(accumulated_sum)
            return False

        try:
            accumulated_sum += float(current_number)
        except ValueError:
            continue

    print_my_sum(accumulated_sum)
    return my_sum(accumulated_sum)


my_sum()

print("The same logic without recursion")
worked = True
current_sum = 0
while worked:
    new_numbers = input("Enter a few numbers separated by a space. For exit enter symbol 'q'. ")
    for number in new_numbers.split():
        if number == "q":
            worked = False
            break

        try:
            current_sum += float(number)
        except ValueError:
            continue

    print_my_sum(current_sum)
