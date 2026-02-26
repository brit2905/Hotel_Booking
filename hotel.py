import json
from booking import Booking
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/bookings.json")  


class Hotel:
    def __init__(self):
        self.rooms = []
        self.bookings = []
        self.load_bookings()  
        
    def add_room(self, room):
        self.rooms.append(room)

    def is_room_available(self, room_number, check_in, check_out):
        for booking in self.bookings:
            if booking.room_number == room_number:
                if check_in < booking.check_out and check_out > booking.check_in:
                    return False
        return True

    def load_bookings(self):
        if not DATA_FILE.exists():
            self.bookings = []
            return

        with open(DATA_FILE, "r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                self.bookings = []
                return

        for item in data:
            check_in_dt = datetime.strptime(item["check_in"], "%Y-%m-%d")
            check_out_dt = datetime.strptime(item["check_out"], "%Y-%m-%d")
            
            booking = Booking(
                item["guest_name"],
                item["room_number"],
                check_in_dt,
                check_out_dt
            )
            self.bookings.append(booking)  
            
    def add_booking(self, booking):
        if self.is_room_available(
            booking.room_number,
            booking.check_in,
            booking.check_out
        ):
            self.bookings.append(booking)
            self.save_bookings()  # ✅ THIS was missing
            print("Booking successful!")
            return True
        else:
            print("Room is not available for those dates.")
            return False

    def save_bookings(self):
        DATA_FILE.parent.mkdir(exist_ok=True)
        
        data = []
        for booking in self.bookings:
            data.append({
                "guest_name": booking.guest_name,
                "room_number": booking.room_number,
                "check_in": booking.check_in.strftime("%Y-%m-%d"),
                "check_out": booking.check_out.strftime("%Y-%m-%d")
            })

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
            
    def get_bookings_by_room(self):
        rooms = {}
        for booking in self.bookings:
            rooms.setdefault(booking.room_number, []).append(booking)
        return rooms
    
    def cancel_booking(self, guest_name, room_number):
        for booking in self.bookings:
            if booking.guest_name == guest_name and booking.room_number == room_number:
                self.bookings.remove(booking)
                self.save_bookings()
                print("Booking cancelled successfully.")
                return
        print("Booking not found.")
        
    def view_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return

        for booking in self.bookings:
            print(
                f"{booking.guest_name} | "
                f"Room {booking.room_number} | "
                f"{booking.check_in.date()} → {booking.check_out.date()}"
            )
