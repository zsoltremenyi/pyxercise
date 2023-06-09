from employee import Employee
import prompting as prm


def validate_input():
    emp = Employee(prm.id(), prm.prompt(), prm.fname(), prm.lname())

    if not emp.employee_id():
        return True
    elif not emp.last_name():
        return True
    elif not emp.first_name():
        return True
    elif not emp.zipcode():
        return True
    elif emp.employee_id() and emp.last_name() and emp.first_name() and emp.zipcode():
        print("There were no errors found.")
        return False