Contact Management System
📌 Project Overview

The Contact Management System is a simple console-based application developed using Python 3. It allows users to manage their contacts by performing Create, Read, Update, and Delete (CRUD) operations.

The project is designed to demonstrate fundamental Python programming concepts, including lists, dictionaries, functions, loops, conditional statements, and input validation.

🎯 Objectives
Create and manage contact records.
Search contacts by name.
Update contact phone numbers.
Delete contacts when they are no longer needed.
Validate phone numbers to ensure they contain exactly 10 digits.
Prevent duplicate phone numbers.
✨ Features
Add Contact — Add a contact with a name, phone number, and email address.
View Contacts — Display all saved contacts.
Search Contact — Search for contacts using a full name or partial name.
Update Contact — Update a contact's phone number.
Delete Contact — Remove a contact and display the remaining contact count.
Phone Validation — Accept only phone numbers containing exactly 10 digits.
Duplicate Prevention — Prevent multiple contacts from using the same phone number.
Menu-Driven Interface — Navigate through the application using a console menu.
🛠️ Technologies Used
Programming Language: Python 3
Data Structures: Lists and Dictionaries
Concepts: Functions, CRUD operations, loops, conditional statements, and input validation
Interface: Command-line interface (CLI)
📂 Project Structure
text
Contact-Management-System/
│
├── contact_management.py
└── README.md

⚙️ Requirements
Python 3 installed on your computer.
A code editor such as Visual Studio Code (optional).

No external Python libraries are required.


🖥️ Application Menu
text
===== CONTACT MANAGEMENT SYSTEM =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Phone
5. Delete Contact
6. Exit

Enter your choice:

🧪 Sample Test Cases
Test Case	Input / Operation	Expected Result
Add Contact	Ravi Sharma, 9876543210, ravi@mail.com	Contact added successfully
Valid Phone Number	Neha Rao, 9999999999	Contact added successfully
Invalid Phone Number	Amit, 98765	Invalid phone number message
Duplicate Phone Number	Reuse 9876543210	Duplicate number rejected
Search Contact	Search for Ravi	Matching contact details displayed
Update Phone	9123456780	Phone number updated successfully
Delete Contact	Delete Neha Rao	Contact deleted and total count displayed
🧠 Concepts Learned
Creating and using Python functions.
Storing records in a list of dictionaries.
Implementing CRUD operations.
Searching and updating records.
Validating user input.
Preventing duplicate phone numbers.
Building a menu-driven console application.
Testing and debugging Python programs.
⚠️ Limitations
Contacts are stored in memory and are lost when the application exits.
The current version updates phone numbers but does not edit names or email addresses.
The application is designed for a single user in a console environment.
🔮 Future Enhancements
Save contacts permanently using CSV or SQLite.
Allow users to update names and email addresses.
Add sorting and advanced search functionality.
Build a graphical user interface using Tkinter.
Add input validation for email addresses.
📚 Conclusion

The Contact Management System is a beginner-friendly Python project that demonstrates how CRUD operations can be implemented using lists, dictionaries, and functions. It provides a foundation for developing more advanced contact management applications with persistent storage and graphical interfaces.

👨‍💻 Author

AHTESHAM ANSARI

GitHub: https://github.com/ahteshamcodes-ai

This project was developed for learning and practicing Python programming fundamentals.
