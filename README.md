This is a simple command-line Library Management System built using Python and MySQL. It supports functionalities for both librarians and users, including book management, user registration, borrowing, and returning books.

on user terminal:

Register with name, email, and password

Login using Gmail and password (hidden using getpass)

View available books

Borrow books

Return borrowed books


Login with default credentials:
librarian
Username: atharva

Password: 8788

Add new books

Delete books

View all users

View borrowed books



install MySQL and create a database:

CREATE DATABASE librarydb;


pip install mysql-connector-python
Run the program:
python library.py

**Note
Password input is hidden using the getpass module for better security.

Librarian login is hardcoded as a default admin access.

Email validation requires @gmail.com for registration and login.



