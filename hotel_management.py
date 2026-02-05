import mysql.connector
from datetime import datetime
import os

# -----------------------------
# Database connection
# -----------------------------
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),  # use environment variable
        database="hotel_db"
    )
    cur = conn.cursor(dictionary=True)
except mysql.connector.Error as e:
    print("Database connection error:", e)
    exit()

# -----------------------------
# Enquiry Function
# -----------------------------
def enquire_room():
    room_type = input("Enter room type (Single/Double/Suite): ")

    try:
        cur.execute("SELECT room_number, price, status FROM rooms WHERE room_type = %s", (room_type,))
        rooms = cur.fetchall()
        available = [r for r in rooms if r["status"] == "Available"]

        if available:
            print(f"\nAvailable {room_type} rooms:")
            for r in available:
                print(f"Room {r['room_number']} → ₹{r['price']} per night")
        else:
            print(f"No {room_type} rooms available right now.")
    except Exception as e:
        print("Error during enquiry:", e)

# -----------------------------
# Booking Function
# -----------------------------
def book_room():
    name = input("Enter customer name: ")
    phone = input("Enter customer phone number: ")
    room_number = input("Enter room number to book: ")
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    # Validate dates
    try:
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        if check_out_date <= check_in_date:
            print("Check-out must be after check-in.")
            return
    except ValueError:
        print("Invalid date format.")
        return

    try:
        # Insert customer
        cur.execute("INSERT INTO customers (name, phone) VALUES (%s, %s)", (name, phone))
        customer_id = cur.lastrowid

        # Find room
        cur.execute("SELECT room_id, price, status FROM rooms WHERE room_number = %s", (room_number,))
        room = cur.fetchone()

        if not room:
            print("Room not found.")
            return

        if room["status"] != "Available":
            print("Room is not available.")
            return

        # Create reservation
        cur.execute("""
            INSERT INTO reservations (customer_id, room_id, check_in, check_out, status)
            VALUES (%s, %s, %s, %s, 'Booked')
        """, (customer_id, room["room_id"], check_in, check_out))
        reservation_id = cur.lastrowid

        # Mark room as booked
        cur.execute("UPDATE rooms SET status = 'Booked' WHERE room_id = %s", (room["room_id"],))
        conn.commit()

        print(f"\nReservation successful! Reservation ID: {reservation_id}")

    except Exception as e:
        print("Booking error:", e)

# -----------------------------
# Billing Function
# -----------------------------
def generate_bill():
    reservation_id = input("Enter reservation ID for billing: ")

    try:
        cur.execute("""
            SELECT r.reservation_id, c.name, c.phone, rm.room_number, rm.price, r.check_in, r.check_out
            FROM reservations r
            JOIN customers c ON r.customer_id = c.customer_id
            JOIN rooms rm ON r.room_id = rm.room_id
            WHERE r.reservation_id = %s
        """, (reservation_id,))
        res = cur.fetchone()

        if not res:
            print("Reservation not found.")
            return

        # Calculate nights
        check_in = datetime.strptime(str(res["check_in"]), "%Y-%m-%d")
        check_out = datetime.strptime(str(res["check_out"]), "%Y-%m-%d")
        nights = max(1, (check_out - check_in).days)
        total = res["price"] * nights

        # Insert bill
        cur.execute("INSERT INTO bills (reservation_id, total_amount) VALUES (%s, %s)", (reservation_id, total))
        conn.commit()

        print("\n=== BILL ===")
        print(f"Customer: {res['name']} ({res['phone']})")
        print(f"Room: {res['room_number']} @ ₹{res['price']} per night")
        print(f"Nights: {nights}")
        print(f"Total: ₹{total}")
        print("============")

    except Exception as e:
        print("Billing error:", e)

# -----------------------------
# Menu System
# -----------------------------
def main_menu():
    while True:
        print("\n--- Hotel Management Menu ---")
        print("1. Enquiry")
        print("2. Booking")
        print("3. Billing")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            enquire_room()
        elif choice == "2":
            book_room()
        elif choice == "3":
            generate_bill()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

# -----------------------------
# Run Program
# -----------------------------
if __name__ == "__main__":
    main_menu()
    cur.close()
    conn.close()
