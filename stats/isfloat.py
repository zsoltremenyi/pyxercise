def is_float(num):
    try:
        number = float(num)
        return True
    except ValueError:
        return False
