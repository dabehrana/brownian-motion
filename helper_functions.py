def get_float_from_user(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            pass


def get_int_from_user(prompt):
    while True:
        try:
            value = int(get_float_from_user(prompt))
            return value
        except ValueError:
            pass
