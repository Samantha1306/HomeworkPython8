from write_data import count_data
import pandas
def input_data():
    dct = dict()
    Id_emp = count_data("employee.csv")
    Id_title = count_data("titles.csv") 
    Id_dept = count_data("departments.csv")
    dct["id_emp"] = Id_emp
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["second_name"] = input('Введите Отчество: ')
    dct["dob"] = input('Введите дату рождения: ')
    dct["city"] = input('Введите Город: ')
    dct["street"] = input('Введите Улицу: ')
    dct["house"] = input('Введите Номер дома: ')
    dct["apartament"] = input('Введите Номер квартиры: ')
    dct["email"] = input('Введите Адрес электронной почты: ')
    dct["phone"] = input('Введите Номер телефона: ')
    dct["id_dept"] = Id_dept
    dct["name_dept"] = input('Введите Название отдела: ')
    dct["id_title"] = Id_title
    dct["name_title"] = input('Введите Название должности: ')
    dct["salary"] = int(input('Введите Размер зарплаты: '))
    return dct