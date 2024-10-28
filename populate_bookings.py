import sqlite3
import datetime
import random
import csv
import populate_reservations as populate_reservations


def populate_bookings(DBbase):
    conn = sqlite3.connect(DBbase)
    cursor = conn.cursor()

    with open('reservations.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

        for row in csv_reader:
            reservation_id, booking_id, lname, fname, zip, DOB = row
            cursor.execute('''INSERT OR REPLACE INTO reservations (reservation_id, booking_id, last_name, first_name, zip, DOB) 
                            VALUES (?, ?, ?, ?, ?, ?)''', 
                            (int(reservation_id), int(booking_id), lname, fname, int(zip), DOB))

    room_types = ["BASIC", "FAMILY", "SUITE", "PENTHOUSE"]
    days_to_book = 30

    for i in range(days_to_book):
        check_in_date = (datetime.datetime.now() + datetime.timedelta(days=i)).strftime("%Y-%m-%d")
        for room_type in room_types:
            cursor.execute("SELECT available FROM rooms WHERE room_type = ?", (room_type,))
            available_rooms = cursor.fetchone()[0]

            #sets ceiling at 10 remaining rooms
            max_bookings = max(0, available_rooms - 10)
            num_bookings = random.randint(0, max_bookings)

            for _ in range(num_bookings):
                nights = random.randint(1, 5)
                check_out_date = (datetime.datetime.strptime(check_in_date, "%Y-%m-%d") + datetime.timedelta(days=nights)).strftime("%Y-%m-%d")

                #insert booking into bookings table and get booking ID
                cursor.execute("INSERT INTO bookings (room_type, check_in, check_out) VALUES (?, ?, ?)", (room_type, check_in_date, check_out_date))
                booking_id = cursor.lastrowid

                #update room availability
                cursor.execute("UPDATE rooms SET available = available - 1 WHERE room_type = ?", (room_type,))


    conn.commit()
    conn.close()
    print("Database populated with bookings and reservations.")

if __name__ == "__main__":
    populate_bookings('hotel_bookings.db')
