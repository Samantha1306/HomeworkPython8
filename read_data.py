

def read_data():
    lst_employee = []
    with open('employee.csv', 'r', encoding="utf_8") as file:
        for line in file:
            temp = line.strip().split(';')
            lst_employee.append(temp)
        print(lst_employee)
    lst_address = []
    with open('address.csv', 'r', encoding="utf_8") as file:
        for line in file:
            temp = line.strip().split(';')
            lst_address.append(temp)
        print(lst_address)

    lst_email = []
    with open('email.csv', 'r', encoding="utf_8") as file:
        for line in file:
            temp = line.strip().split(';')
            lst_email.append(temp)
        print(lst_email)

    lst_phone = []
    with open('phone.csv', 'r', encoding="utf_8") as file:
        for line in file:
            temp = line.strip().split(';')
            lst_phone.append(temp)
        print(lst_phone)

    lst_departments = []
    with open('departments.csv', 'r', encoding="utf_8") as file:
        for line in file:
            temp = line.strip().split(';')
            lst_departments.append(temp)
        print(lst_departments)

    lst_titles = []
    with open('titles.csv', 'r', encoding="utf_8") as file:
        for line in file:
            temp = line.strip().split(';')
            lst_titles.append(temp)
        print(lst_titles)
    lst = []
    for i in range(len(lst_employee)):
        lst.append([lst_employee[i][0], lst_employee[i][1], lst_employee[i][2], lst_employee[i][3], lst_employee[i][4], lst_employee[i][5], lst_employee[i][6],
                    lst_address[i][1], lst_address[i][2], lst_address[i][3], lst_address[i][4],
                    lst_email[i][1],
                    lst_phone[i][1],
                    lst_departments[i][1],
                    lst_titles[i][1], lst_titles[i][2]])
    return lst
