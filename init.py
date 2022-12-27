from read_data import read_data


def init():
    if not (len(read_data()) > 0):

        with open("employee.csv", 'a+', encoding="utf_8") as file:
            file.write("id_emp;surname;name;second_name;dob;id_title;id_dept\n")
        with open("address.csv", 'a+', encoding="utf_8") as file:
            file.write("id_emp;city;street;house;apartament\n")
        with open("email.csv", 'a+', encoding="utf_8") as file:
            file.write("id_emp;email\n")
        with open("phone.csv", 'a+', encoding="utf_8") as file:
            file.write("id_emp;phone\n")
        with open("departments.csv", 'a+', encoding="utf_8") as file:
            file.write("id_dept;name_dept\n")
        with open("titles.csv", 'a+', encoding="utf_8") as file:
            file.write("id_title;name_title;salary\n")
