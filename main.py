from rooms import rooms_management
from menus import main_menu
from i_o import get_and_validate
from validators_and_helpers import is_digit
from bookings import orders_management

def main():
    choice = ''
    while choice != '6':
        main_menu()
        choice = get_and_validate("Choose an option: ", is_digit)
        if choice == '1':
            rooms_management()

        elif choice == '2':
            orders_management()

        elif choice != '6':
            print("Choice must be 1-6")

if __name__ == "__main__":
    main()