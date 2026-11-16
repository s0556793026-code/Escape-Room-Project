from menus import show_order_menu, update_order_menu
from i_o import get_and_validate
from validators_and_helpers import  search_order_by_date ,search_order_by_customer_name ,is_order_exist ,search_order_by_id ,search_room_by_id ,is_valid_time ,is_digit, is_not_empty, is_room_exist_and_activite, is_valid_date
from manage_data import load_data, read_and_update_data
import datetime


def add_time():
    return time

def add_players(room):
    
    players = 100
    max_players = room[0]["max_players"]
    while players > max_players:
        choice = get_and_validate("Enter number of participants: ", is_digit)
        players = int(choice)
        if players <= max_players:
            return players
        print(f"Maximum players in the room is {max_players} Try again")
        
def group_discount(price, precent):
    return price - (price / 100 * precent)

def weekend_discount(price, date):
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    if date.weekday() in (4, 5):
        return price - (price / 100 * 15)
    return price

def total_price(room, players, date):
    price_per_player = room[0]["price_per_player"]
    price = players * price_per_player
    if players >= 5:
        price = group_discount(price, 10)
    elif players >= 7:
        price = group_discount(price, 15)
    
    price = weekend_discount(price, date)

    return round(price, 2)




def add_order():
    booking_id = max(int(room["booking_id"][1:]) for room in load_data("bookings.json")) + 1
    customer_name = get_and_validate("Enter your name: ", is_not_empty)
    room_id = get_and_validate("Enter room id: ", is_room_exist_and_activite)
    room  = search_room_by_id(room_id, load_data("rooms.json"))
    booking_date = get_and_validate("Enter the date in format Y-m-d: ", is_valid_date)
    start_time = get_and_validate("Enter time in format 00:00: ", is_valid_time)
    players = add_players(room)
    price = total_price(room, players, booking_date)

    return {
        "booking_id": f"B{str(booking_id).zfill(3)}",
        "customer_name": customer_name,
        "room_id": room[0]["room_id"],
        "booking_date": booking_date,
        "start_time": start_time,
        "players": players,
        "total_price": price,
        "status": "Active",
        "cancellation_fee": 0.0
    }

def show_bookings():
    for order in load_data("bookings.json"):
        print(order, '\n\n')

def update(booking_id, value, parameter):
    data = load_data("bookings.json")
    for order in data:
        if order["booking_id"] ==f"B{booking_id.zfill(3)}":
            order[parameter] = value
    read_and_update_data("bookings.json", data)

def update_order():
    booking_id = get_and_validate("Enter order id: ", is_order_exist)
    choice = ''
    while choice != '4':
        update_order_menu()
        choice = get_and_validate("Choose an option: ", is_digit)
        if choice == '1':
            booking_date = get_and_validate("Enter the date in format Y-m-d: ", is_valid_date)
            update(booking_id, booking_date, "booking_date")
        elif choice == '2':
            start_time = get_and_validate("Enter time in format 00:00: ", is_valid_time)
            update(booking_id, start_time, "start_time")
        elif choice == '3':
            room_id = search_order_by_id(booking_id, load_data("bookings.json"))[0]["room_id"][-1]
            room  = search_room_by_id(room_id, load_data("rooms.json"))
            players = add_players(room)
            update(booking_id, players, "players")
        elif choice != '4':
            print("Choice must be 1-4")

def cancellation_fees(start_time, booking_date, total_price):
    date = f"{booking_date} {start_time}"
    diff = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M' ) - datetime.datetime.now()
    if diff < datetime.timedelta(hours=6):
        return total_price / 2
    
    elif diff <= datetime.timedelta(hours=24):
        return total_price / 4

    else:
        return 0.0


def cancel_order():
    data = load_data("bookings.json")
    booking_id = get_and_validate("Enter order id: ", is_order_exist)
    for order in data:
        if order["booking_id"] == f"B{booking_id.zfill(3)}":
            if order["status"] == "Active":
                order["status"] = "Cancelled"
                order["cancellation_fee"] = cancellation_fees(order["start_time"],order["booking_date"], order["total_price"])
                print("Order successfully cancelled")
            else:
                print("The order has already been cancelled.")

    read_and_update_data("bookings.json", data)

def orders_management():
    choice = ''
    while choice != '8':
        show_order_menu()
        choice = get_and_validate("Choose an option: ",is_digit)
        if choice == '1':
            order = add_order()
            data = load_data("bookings.json")
            data.append(order)
            read_and_update_data("bookings.json",data)

        elif choice == '2':
            show_bookings()

        elif choice == '3':
            data = load_data("bookings.json")
            booking_id = get_and_validate("Enter order id: ", is_order_exist)
            print(search_order_by_id(booking_id, data))

        elif choice == '4':
            data = load_data("bookings.json")
            customer_name = get_and_validate("Enter customer name: ", is_not_empty)
            print(search_order_by_customer_name(customer_name, data))
        
        elif choice == '5':
            booking_date = get_and_validate("Enter the date in format Y-m-d: ", is_valid_date)
            data = load_data("bookings.json")
            print(search_order_by_date(booking_date, data))

        elif choice == '6':
            update_order()

        elif choice == '7':
            cancel_order()

        elif choice != '8':
            print("Choice must be 1-8")


