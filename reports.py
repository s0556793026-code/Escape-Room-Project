from menus import show_reports_menu
from manage_data import load_data
from i_o import get_and_validate
from validators_and_helpers import is_digit, is_room_exist_and_activite

def show_orders_by_status(value):
    data = load_data("bookings.json")
    if data:
        for order in data:
            if order["status"] == value:
                print(order, '\n\n')
    else:
        print("There are no orders yet.")

def show_revenue():
    data = load_data("bookings.json")
    sum_revenue = sum(order["total_price"] for order in data if order["status"] == "Active")
    print(f'Revenue from active orders = {sum_revenue}')

def total_cancellation_fees():
    data = load_data("bookings.json")
    sum_fees = sum(order["cancellation_fee"] for order in data if order["status"] == "Cancelled")
    print(f'Total cancellation fees = {sum_fees}')

def count_room():
    data = load_data("bookings.json")
    count_dict = {}
    for order in data:
        if order["status"] == 'Active':
            if order["room_id"] in count_dict:
                count_dict[order["room_id"]] += 1
            else:
                count_dict[order["room_id"]] = 1

    return count_dict

def popularest_room():
    count_dict = count_room()
    max_count = [key for key, value in count_dict.items() if value == max(count_dict.values())]
    print(f"The most popular room is: {max_count}")

def room_occupancy_rate():
    room_id = get_and_validate("Enter room id: ", is_room_exist_and_activite)
    room_id = f"R{room_id.zfill(3)}"
    data_bookings = load_data("bookings.json")
    data_rooms = load_data("rooms.json")
    duration = [room["duration"] for room in data_rooms if room["room_id"] == room_id][0]
    count_room = len([order for order in data_bookings if order["room_id"] == room_id and order["status"] == "Active"])
    room_occupancy = round(100 / 12 * (count_room * duration / 60) , 2)
    print(f"Room occupancy rate for room {room_id} is: {room_occupancy} %")

def management_reports():
    choice = ''

    while choice != '8':
        show_reports_menu()
        choice = get_and_validate("Choose an option: ", is_digit)
        if choice == '1':
            show_orders_by_status("Active")
        
        elif choice == '2':
            show_orders_by_status("Cancelled")

        elif choice == '3':
            show_revenue()

        elif choice == '4':
            total_cancellation_fees()
        
        elif choice == '5':
            popularest_room()

        elif choice == '6':
            print(count_room())

        elif choice == '7':
            room_occupancy_rate()

        elif choice != '8':
            print("Choice must be 1-8")
