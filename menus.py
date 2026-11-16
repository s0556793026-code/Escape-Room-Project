def main_menu():
    print("""
--------------------------
        MAIN MENU
--------------------------

1. Management rooms
2. Management orders
3. Management Reports and Data
4. Exit
       
    """
    )




def show_rooms_menu():
    print("""
--------------------------
  ESCAPE ROOM MANAGEMENT
--------------------------

1. Display all rooms
2. Search room details
3. Add new room
4. Update room details
5. Activate or deactivate room
6. Back to Main Menu
       
    """
    )

def show_order_menu():
    print("""
--------------------------
 ORDERS MANAGEMENT
--------------------------

1. Add new order
2. Display all orders
3. Search order by ID 
4. Display orders by customer 
5. Display orders by date
6. Update order
7. Order Cancellation
8. Back to main menu
       
    """
    )

def show_reports_menu():
    print("""
--------------------------
    REPORTS MANAGEMENT
--------------------------

1. Display total active orders
2. Display total cancelled orders
3. Display total revenue from active orders
4. Display total cancellation fees from cancelled bookings
5. Display the most popular room
6. Display number of bookings per room
7. Display occupancy rate of a specific room on a given date
8. Back to Main Menu
    """
    )


def update_room_menu():
    print("""
--------------------------
    UPDATE ROOM
--------------------------

1. Update room name
2. Update room difficulty
3. Update room duration
4. Update minimum players
5. Update maximum players
6. Update price per player
7. Back to Main Menu
    """
    )

def update_order_menu():
    print("""
--------------------------
    UPDATE BOOKING
--------------------------

1. Update order date
2. Update order start time
3. Update מumber of participants
4. Back to Main Menu
    """)
    
