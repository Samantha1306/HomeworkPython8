from input_data import input_data
from write_data import write_data


def push_data():
    dct = input_data()

    write_data([dct.get("id_emp"), dct.get("surname"), dct.get("name"), dct.get("second_name"), dct.get("dob"), dct.get("id_title"), dct.get("id_dept")], "employee.csv")

    write_data([dct["id_emp"], dct["city"], dct["street"], dct["house"], dct["apartament"]], "address.csv")

    write_data([dct["id_emp"], dct["email"]], "email.csv")

    write_data([dct["id_emp"], dct["phone"]], "phone.csv")
    
    write_data([dct["id_dept"], dct["name_dept"]], "departments.csv")

    write_data([dct["id_title"], dct["name_title"], dct["salary"]], "titles.csv")