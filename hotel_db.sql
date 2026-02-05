CREATE DATABASE IF NOT EXISTS hotel_db;
USE hotel_db;

CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_number INT UNIQUE,
    room_type VARCHAR(20),
    price INT,
    status VARCHAR(20)
);

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE reservations (
    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    room_id INT,
    check_in DATE,
    check_out DATE,
    status VARCHAR(20),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (room_id) REFERENCES rooms(room_id)
);

CREATE TABLE bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT,
    total_amount INT,
    FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id)
);

INSERT INTO rooms (room_number, room_type, price, status) VALUES
(101, 'Single', 1000, 'Available'),
(102, 'Single', 1000, 'Available'),
(201, 'Double', 1800, 'Available'),
(202, 'Double', 1800, 'Available'),
(301, 'Suite', 3000, 'Available');
