# Hospital-Management-System
This project stores and retrieve the patients and doctors data from the database

🏥 Hospital Management System (Python + MySQL)
📌 Project Description

This is a Python-based Hospital Management System developed using MySQL Connector.
The project allows users to manage patients and doctors data efficiently by storing and retrieving information from a MySQL database.

The system is menu-driven and supports basic CRUD operations like adding and viewing records.


🎯 Project Objectives
   * To understand database connectivity using Python
   * To perform insert and fetch operations in MySQL
   * To manage patient and doctor records efficiently
   * To build a menu-driven real-world application
   * To strengthen backend development concepts

🛠 Technologies Used
   * Python
   * MySQL
   * MySQL Connector (mysql-connector-python)

⚙️ Features
   * Add Patient
     Stores patient details such as:
      Name
     -> Age
     -> Gender
     -> Disease
       
   * Add Doctor
     Stores doctor details such as:
     -> Name
     -> Age
     -> Gender
     -> Specialization

   * View Patients
     Displays all existing patient records from the database.

   * View Doctors
     Displays all existing doctor records from the database.

   * Exit
     Safely exits the program.


📋 How It Works
* The user selects options from a menu.
* Based on the selected option, data is either inserted into or fetched from the MySQL database.
* The program continues running until the user chooses the exit option.

🚀 How to Run
* Install required package:
    -------    pip install mysql-connector-python
* Create the required database and tables in MySQL.
* Update database credentials in the Python file.
* Run the project:
   ---------   python main.py

📌 Key Learnings
   * Python–MySQL connectivity
   * SQL queries (INSERT, SELECT)
   * Menu-driven programming
   * Modular function design
   * Console-based application development
