
def get_float_from_user(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("\n\033[31m" + 
            "Invalid value. Please try again..." +
            "\033[0m")
            pass


def get_int_from_user(prompt):
    while True:
        try:
            value = int(get_float_from_user(prompt))
            return value
        except ValueError:
            print("\n\033[31m"+
            "Invalid value. Please try again..." +
            "\033[0m")
            pass
