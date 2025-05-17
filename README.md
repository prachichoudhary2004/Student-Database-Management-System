

 🎓 Student Database Management System

This repository contains a Python-based Student Database Management System that leverages MySQL to perform robust database operations. The system provides a simple, efficient interface to manage student records through essential CRUD (Create, Read, Update, Delete) functionalities.

---

 ✨ Features

➕ Add New Student
Easily add new student information into the database with fields such as name, roll number, contact details, and more.

📋 View Students
Retrieve and display a complete list of all student records stored in the system.

✏️ Update Student
Modify existing student details to keep the database accurate and up-to-date.

❌ Delete Student
Remove student records permanently from the database when required.

🔎 Search Student
Search for students based on various criteria like name, roll number, or department, enabling quick access to specific records.

---

 🛠️ Technologies Used

 Programming Language: Python 3.x
 Database: MySQL Server
 Connector: MySQL Connector/Python (mysql-connector-python)

---

 🧰 Prerequisites

 Python 3.x installed on your system
 MySQL Server installed and running
 MySQL Connector for Python installed (you can install it via pip):

  ```bash
  pip install mysql-connector-python
  ```

---

 🚀 Installation & Setup

1. Clone the repository

   ```bash
   git clone https://github.com/prachichoudhary2004/Student-Database-Management-System.git
   cd Student-Database-Management-System
   ```

2. Configure the database

    Open your MySQL client (e.g., MySQL Workbench, phpMyAdmin, or command line)
    Create a new database (e.g., `student_db`)
    Import the provided SQL schema if available, or create tables as per the project documentation

3. Update database connection details

    Open the Python script file where the MySQL connection is established
    Set your MySQL username, password, and database name accordingly

4. Run the application

   ```bash
   python main.py
   ```

--

 🗂️ Project Structure

```
Student-Database-Management-System/
├── main.py                Main program file handling CRUD operations
├── db_config.py           Database connection setup
├── requirements.txt       Python dependencies
├── README.md              Project documentation
└── schema.sql             (Optional) SQL file to set up database schema
```

---

 📸 Screenshot

![Screenshot (67)](https://github.com/user-attachments/assets/8f7d083c-edc3-4b15-839b-0885d0fab556)

---

 🚀 Future Enhancements

 Build a GUI interface using Tkinter or PyQt for better user interaction
 Implement user authentication and role-based access
 Add export/import functionality (CSV, Excel) for bulk student data handling
 Integrate with web-based frontends for easier accessibility

---

 🙋‍♀️ About the Developer

Prachi Choudhary
💻 Enthusiastic about database systems and Python programming

GitHub: [@prachichoudhary2004](https://github.com/prachichoudhary2004)
Email: [prachichoudhary2004@gmail.com](mailto:prachichoudhary2004@gmail.com)


> “Managing student data effectively is the foundation of efficient educational administration.”
