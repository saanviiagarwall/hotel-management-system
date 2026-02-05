# 🏨 Hotel Management System (Python + MySQL)

A simple command-line Hotel Management System developed using Python and MySQL.  
This project allows hotel staff to manage room enquiries, bookings, and billing efficiently.

Built as a school project to demonstrate database integration and real-world application logic.

---

## 🚀 Features

- Room enquiry by room type (Single / Double / Suite)
- Room booking with customer details
- Check-in and check-out date handling
- Automatic bill generation based on stay duration
- MySQL database integration
- Menu-driven command-line interface

---

## 🛠 Tech Stack

- Language: Python  
- Database: MySQL  
- Library: mysql-connector-python  

---

## 📦 Project Structure

hotel-management-system/
│
├── hotel_management.py   # Main program
├── README.md             # Project documentation
├── LICENSE
└── .gitignore

---

## ⚙️ Installation & Setup

### 1) Install requirements
pip install mysql-connector-python

### 2) Setup MySQL database

Create a database named:
hotel_db

Create tables:
- rooms
- customers
- reservations
- bills

### 3) Set MySQL password as environment variable

Windows (PowerShell):
setx MYSQL_PASSWORD "yourpassword"

Mac/Linux:
export MYSQL_PASSWORD="yourpassword"

### 4) Run the program
python hotel_management.py

---

## 📸 How It Works

1. User selects an option from the menu  
2. System checks database for room availability  
3. Booking is stored in MySQL  
4. Billing is generated based on stay duration  

---

## 🎯 Learning Outcomes

- Database connectivity using Python  
- CRUD operations in MySQL  
- SQL joins and relational design  
- CLI-based application structure  
- Basic input validation and error handling  

---

## 🔮 Future Improvements

- GUI version (Tkinter / Web app)
- Login system (Admin/Staff)
- Room availability by date
- Checkout & cancellation feature
- Reports dashboard

---

## 👤 Author

Student project built for learning Python and database integration.

---

## 📜 License

This project is licensed under the MIT License — feel free to use and learn from it.

