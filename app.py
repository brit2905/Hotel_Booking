from flask import Flask, render_template, request, redirect, flash
from hotel import Hotel
from booking import Booking
from datetime import datetime

app = Flask(__name__)
# This is the secret key. You can make it any string you want.
app.secret_key = "luxury_hotel_2026_key" 

hotel = Hotel()

@app.route("/")
def home():
    total_rooms = 10 
    current_bookings = len(hotel.bookings)
    available_rooms = total_rooms - current_bookings
    return render_template("index.html", rooms_left=available_rooms)

@app.route("/add-booking", methods=["POST"])
def add_booking():
    guest_name = request.form["guest_name"]
    room_number = int(request.form["room_number"])
    check_in = datetime.strptime(request.form["check_in"], "%Y-%m-%d")
    check_out = datetime.strptime(request.form["check_out"], "%Y-%m-%d")

    booking = Booking(guest_name, room_number, check_in, check_out)
    
    # This calls hotel.py and gets the True/False result
    success = hotel.add_booking(booking) 

    if success:
        flash("Success! Your room is reserved.", "success")
    else:
        flash("Sorry, that room is already booked for those dates.", "error")

    return redirect("/")

@app.route("/cancel-booking", methods=["POST"])
def cancel_booking():
    guest_name = request.form["guest_name"]
    room_number = int(request.form["room_number"])
    
    # This calls your existing logic in hotel.py
    # Note: You might want to update hotel.py to return True/False like we did for adding!
    hotel.cancel_booking(guest_name, room_number)
    
    flash(f"Booking for {guest_name} has been cancelled.", "success")
    return redirect("/")
        
if __name__ == "__main__":
    app.run(debug=True)