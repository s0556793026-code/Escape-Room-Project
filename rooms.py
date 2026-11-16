from menus import show_rooms_menu, update_room_menu
from validators_and_helpers import is_digit, is_not_empty, is_room_exist, is_in_difficulty, search_room_by_id, is_bool
from i_o import get_and_validate
from manage_data import load_data, read_and_update_data


def show_all_rooms(data):
    for room in data:
        print(room, '\n\n')

def show_room_by_id(room_id):
    data = load_data("rooms.json")
    room = search_room_by_id(room_id,data)
    if room:
        print(room)
    else:
        print("Room not exist")

def add_difficulty():
    difficulty = get_and_validate("Enter difficulty, 1. Easy, 2. Hard, 3. Medium: ", is_in_difficulty)
    if difficulty == '1':
        difficulty = 'Easy'
    elif difficulty == '2':
        difficulty = 'Hard'
    else:
        difficulty = 'Medium'
    return difficulty


def add_room():
    name = get_and_validate("Enter room name: ", is_not_empty)

    difficulty = add_difficulty()

    duration = get_and_validate("Enter game duration in minutes: ", is_digit)

    min_players = get_and_validate("Enter minimum players: ", is_digit)

    max_players = get_and_validate("Enter maximum players: ", is_digit)

    price_per_player = get_and_validate("Enter price per player: ", is_digit)
    
    room_id = max(int(room["room_id"][1:]) for room in load_data("rooms.json")) + 1

    return {
        "room_id": f"R{str(room_id).zfill(3)}",
        "name": name,
        "difficulty": difficulty,
        "duration": int(duration),
        "min_players": int(min_players),
        "max_players": int(max_players),
        "price_per_player": int(price_per_player),
        "is_active": True
    }
def update_room():
    room_id = get_and_validate("Enter room id: ", is_room_exist)
    choice = ''
    while choice != '7':
        update_room_menu()
        choice = get_and_validate("Choose an option: ", is_digit)

        if choice == '1':
            name = get_and_validate("Enter room name: ", is_not_empty)
            update_room_details(name, "name")
        elif choice == '2':
            difficulty = add_difficulty()
            update_room_details(difficulty, "difficulty")
        elif choice == '3':
            duration = get_and_validate("Enter game duration in minutes: ", is_digit)
            update_room_details(duration, "duration")
        elif choice == '4':
            min_players = get_and_validate("Enter minimum players: ", is_digit)
            update_room_details(min_players, "min_player")
        elif choice == '5':
            max_players = get_and_validate("Enter maximum players: ", is_digit)
            update_room_details(max_players, "max_player")
        elif choice == '6':
            price_per_player = get_and_validate("Enter price per player: ", is_digit)
            update_room_details(price_per_player, "price_per_player")
        elif choice != '7':
            print("Choice must be 1-7")


def update_room_details(choice, parameter):
    data = load_data("rooms.json")
    for room in data:
        room[parameter] = choice
    read_and_update_data("rooms.json", data)

def change_activate(room_id):
    data = load_data("rooms.json")
    for room in data:
        if room["room_id"] == f"R00{room_id}":
            if room["is_active"]:
                room["is_active"] = False
            else:
                room["is_active"] = True

    read_and_update_data("rooms.json", data)


def rooms_management():
    choice  = ''
    while choice != '6':
        show_rooms_menu()
        choice = get_and_validate("Choose an option: ", is_digit)
        if choice == '1':
            data = load_data("rooms.json")
            show_all_rooms(data)
        elif choice == '2':
            room_id = get_and_validate("Enter room id: ", is_digit)
            show_room_by_id(room_id)

        elif choice == '3':
            new_room = add_room()
            data = load_data("rooms.json")
            data.append(new_room)
            read_and_update_data("rooms.json", data)

        elif choice == '4':
            update_room()

        elif choice == '5':
            room_id = get_and_validate("Enter room id: ", is_room_exist)
            change_activate(room_id)

        elif choice != '6':
            print("Choice must be 1-6")

