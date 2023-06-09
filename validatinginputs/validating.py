from employee import Employee
import prompting as prm
import validateInput as vi


flag = True


while flag:
    if not vi.validate_input():
        flag = False
    else:
        continue