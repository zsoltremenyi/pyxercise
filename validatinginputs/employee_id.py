def employee_id(id):
    if len(id) == 7:
        if id[:2].isalpha() and id[2] == "-" and id[3:].isdigit():
            return id
        else:
            return f"Invalid ID: {id}\n" \
                   f"A valid ID has the format: AA-1234\nPlease check."
    return "Check length of ID."


print(employee_id("1f-4821"))