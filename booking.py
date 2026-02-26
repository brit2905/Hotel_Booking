from datetime import datetime

class Booking:
    def __init__(self, guest_name, room_number, check_in, check_out):
       self.guest_name = guest_name
       self.room_number = room_number
       # We remove the strptime conversion because the data is already a date
       self.check_in = check_in
       self.check_out = check_out