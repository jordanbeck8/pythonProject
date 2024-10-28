import csv
import random
import datetime
import names

def generate_reservation_data(num_entries, filename="reservations.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["reservation_id", "booking_id", "last_name", "first_name", "zip", "DOB"])

        for row in range(1, num_entries + 1):
            reservation_id = row
            booking_id = row
            lname = names.get_last_name()
            fname = names.get_first_name()
            zip = random.randint(10000, 99999)
            #random age between 18 and 80 years old
            DOB = (datetime.datetime.now() - datetime.timedelta(days=random.randint(18 * 365, 80 * 365))).strftime("%Y-%m-%d")

            writer.writerow([reservation_id, booking_id, lname, fname, zip, DOB])

    print(f"{num_entries} entries written to {filename}.")

#creates a CSV file with 1000 rows of data that match the reservations table
generate_reservation_data(1000)
