from employee import Employee
import prompting as prm


flag = True


while flag:
    emp = Employee(prm.id(), prm.prompt(), prm.fname(), prm.lname())

    if not emp.employee_id():
        print()
    elif not emp.last_name():
        print()
    elif not emp.first_name():
        print()
    elif not emp.zipcode():
        print()
    elif emp.employee_id() and emp.last_name() and emp.first_name() and emp.zipcode():
        print("There were no errors found.")
        flag = False



