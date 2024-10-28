import csv
import random
import datetime
import names

def generate_reservation_data(num_entries, filename="reservations.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["reservation_id", "booking_id", "last_name", "first_name", "billing_zip", "date_of_birth"])

        for row in range(1, num_entries + 1):
            reservation_id = row
            booking_id = random.randint(1, 100)
            last_name = names.get_last_name()
            first_name = names.get_first_name()
            billing_zip = random.randint(10000, 99999)
            date_of_birth = (datetime.datetime.now() - datetime.timedelta(days=random.randint(18 * 365, 80 * 365))).strftime("%Y-%m-%d")

            writer.writerow([reservation_id, booking_id, last_name, first_name, billing_zip, date_of_birth])

    print(f"{num_entries} entries written to {filename}.")

#creates a CSV file with 1000 rows of data that match the reservations table
generate_reservation_data(1000)
