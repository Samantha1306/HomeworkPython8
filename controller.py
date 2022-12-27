
from push_data import *
from read_data import *
from print_data import *
from search_data import *


def greet():
    print("Добрый день! Вы зашли в информационную систему для работы с сотрудниками компании.\n\
    С помощью нее вы можете получить данные о сотрудниках, добавить сотрудника, найти сотрудника.\n\
    Для того, чтобы выбрать необходимое действие, введите нужную цифру из меню.")

def menu():
    print("Меню:\n\
    1 - получить всю информацию о сотрудниках;\n\
    2 - получить информацию о сотрудниках без адреса;\n\
    3 - получить только адреса сотрудников;\n\
    4 - добавить сотрудника;\n\
    5 - поиск сотрудника;\n\
    6 - выход.")
    num = int(input("Введите цифру: "))
    while True:
        if num == 1:
            data = read_data()
            print_data(data)
            menu()
        elif num == 2:
            data = read_data()
            print_employee_data(data)
            menu()
        elif num == 3:
            data = read_data()
            print_address(data)
            menu()
        elif num == 4:
            push_data()
            menu()
        elif num == 5:
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Данные не обнаружены")                
            menu()
        elif num == 6:
            print("Работа с системой завершена")
            break
