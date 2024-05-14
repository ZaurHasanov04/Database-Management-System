# Database Management System

This is a simple database management system built in Python using the Click library and SQLite3.

## Features

- Create tables in the database
- Insert data into tables
- Select data from tables

## Installation

1. Clone the repository:

```bash
git clone [<repository_url>](https://github.com/ZaurHasanov04/Database-Management-System.git)



# Requirements
pip install -r requirements

# USAGE

Make sure you have Python installed on your system.

Run the following command to create a table:
python <filename>.py create_table --query "<SQL_QUERY>"
Replace <filename> with the name of your Python file and <SQL_QUERY> with the SQL query to create a table.

# Example
python main.py create_table --query "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)"
This command will create a table named users with three columns: id, name, and email.
python main.py insert --query "INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com')"
This command will insert a new record into the users table.

# Future Plans
Implement authentication to secure access to the database management system.


