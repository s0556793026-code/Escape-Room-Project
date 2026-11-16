import json


def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("Database file is corrupted - starting empty")
        return []
    
    return data
    
def read_and_update_data(file_name, order):
    data =  load_data(file_name)
    if data:
        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(order, file, indent=2, ensure_ascii=False)
    else:
        print("Data not found")