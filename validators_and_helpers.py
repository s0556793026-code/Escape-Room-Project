from manage_data import load_data
import datetime


data = load_data("rooms.json")


def is_digit(choice):
    if choice.isdigit():
        return True

    print("Choice must be a number Try again")
    return False

def is_not_empty(name):
    if name.strip():
        return True

    print("Name cannot be empty. Try again")
    return False


def is_in_range(choice, stop):
    if int(choice) in range(1, stop + 1):
        return True
    print(f"Choice must be 1-{stop}")
    return False


def is_in_difficulty(choice):
    if is_digit(choice):
        if is_in_range(choice, 3):
            return True

def is_room_exist(room_id):
    if is_digit(room_id):
        for room in data:
            if room["room_id"] == f"R00{room_id}":
                return True

        print("Room not exist. Try again")
        return False

    return False
data_orders = load_data("bookings.json")

def is_order_exist(booking_id):
    if is_digit(booking_id):
        for order in data_orders:
            if order["booking_id"] == f"B{booking_id.zfill(3)}":
                return True

        print("Order not exist. Try again")
        return False

    return False

data = load_data("rooms.json")


def search_room_by_id(room_id, data):
    return [room for room in data if room["room_id"] == f"R00{room_id}"]

def search_order_by_id(booking_id, data):
    return [order for order in data if order["booking_id"] == f"B{booking_id.zfill(3)}"]

def search_order_by_customer_name(customer_name, data):
    return [order for order in data if order["customer_name"].lower() == customer_name.lower()]

def search_order_by_date(booking_date, data):
    return [order for order in data if order["booking_date"] == booking_date]




def is_bool(choice):
    if choice  == '1':
        return True
    return False

def is_room_exist_and_activite(room_id):
    data = load_data("rooms.json")
    if is_room_exist(room_id):
        room = search_room_by_id(room_id, data)
        if room[0]["is_active"]:
            return True

        print("Room occupied")
        return False

    return False


def is_valid_date(date_first):
    try:
        if datetime.date.today() <= datetime.date.strptime(date_first, '%Y-%m-%d'):
            return True
        print("Date has already passed. Try again")
        return False
    except Exception as e:
        print(e)
        return False

def is_valid_time(time_add):
    try:
        if datetime.time(10,0) <= datetime.time.strptime(time_add, '%H:%M') <= datetime.time(22,0) :
            return True
        print("Hour must be 10-22. Try again")
        return False
    except Exception as e:
        print(e)
        return False
