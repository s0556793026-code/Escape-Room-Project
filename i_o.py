

def get_and_validate(msg, validation):
    is_valid = False
    while not is_valid:
        choice = input(msg)
        is_valid = validation(choice)

    return choice