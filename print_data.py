def print_data(data, search = False):
    if len(data) > 0:
        print("id_emp", "Фамилия", "Имя", "Отчество", "Дата рождения", "id_title", "id_dept",\
            "Город", "Улица", "Номер дома", "Номер квартиры",\
            "Адрес электронной почты", "Номер телефона",\
            "Название отдела", "Название должности", "Размер зарплаты")
        print("-"*120)
        if not search:
            del data[0]
        for item in data:
            print(item[0], item[1], item[2], item[3], item[4], item[5], item[6],\
            item[7], item[8], item[9],\
            item[10], item[11],\
            item[12], item[13], item[14], item[15])
    else:
        print("\n")
        print("*"*100 + "\nСправочник пуст!\n" + "*"*100)
        print("\n")

def print_employee_data(data, search = False):
    if len(data) > 0:
        print("id_emp".center(4), "Фамилия".center(10), "Имя".center(8), "Отчество".center(10), "Дата рождения".center(10), "id_title".center(10), "id_dept".center(10),\
            "Адрес электронной почты".center(10), "Номер телефона".center(10),"Размер зарплаты".center(10))
        print("-"*120)
        if not search:
            del data[0]
        for item in data:
            print(item[0].center(4), item[1].center(10), item[2].center(10), item[3].center(10), item[4].center(10), item[5].center(15), item[6].center(10),\
            item[11].center(10), item[12].center(30),item[15].center(10))
    else:
        print("\n")
        print("*"*100 + "\nСправочник пуст!\n" + "*"*100)
        print("\n")

def print_address(data, search = False):
    if len(data) > 0:
        print("id_emp".center(4), "Город".center(20), "Улица".center(20), "Номер дома".center(10), "Номер квартиры".center(10))
        print("-"*120)
        if not search:
            del data[0]
        for item in data:
            print(item[0].center(4), item[7].center(20), item[8].center(20), item[9].center(10), item[10].center(10))
    else:
        print("\n")
        print("*"*100 + "\nСправочник пуст!\n" + "*"*100)
        print("\n")        
