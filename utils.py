def getIntegerValueFromUser(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            pass