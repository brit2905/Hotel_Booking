from room import Room 
from booking import Booking
from hotel import Hotel

hotel = Hotel()
# Add rooms (hardcoded for now)
hotel.add_room(Room(101, "single", 500))
hotel.add_room(Room(102, "double", 800))

while True:
    print("\nHotel Booking System")
    print("1. Add booking")
    print("2. View bookings")
    print("3. Cancel booking")
    print("4. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        name = input("Guest name: ")
        room = int(input("Room number: "))
        check_in = input("Check-in(YYYY-MM-DD): ")
        check_out = input("Check-out (YYYY-MM-DD): ")
        
        booking = Booking(name, room, check_in, check_out)
        hotel.add_booking(booking)
        
    elif choice == "2":
        if not hotel.bookings:
            print("No bookings found.")
        else:
            for b in hotel.bookings:
                print(
                    f"{b.guest_name} | Room {b.room_number} | "
                    f"{b.check_in.date()}  → {b.check_out.date()} "
                )
    
    elif choice == "3":
        hotel.view_bookings()
        name = input("Guest name to cancel: ")
        room = int(input("Room number to cancel: "))
        confirm = input("Are you sure you want to cancel this booking? (y/n): ")
        if confirm.lower() == "y":
            hotel.cancel_booking(name, room)
        else:
            print("Cancellation aborted. ")
    
    elif choice == "4":
        print("Thank you for visiting our page. Goodbye 👋")
        break
    
    else:
        print("Invalid option. Please try agian.")
    