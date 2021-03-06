import sqlite3
from sqlite3 import Error

# INSERT PERSON ENTRY QUERY
create_person = """
INSERT INTO
  people (name, surname, email, birthday, nameday, address, interests, phone, socials)
VALUES
  (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

# SELECT PERSON QUERY
select_all_query = """
SELECT
 *
FROM
  people
"""
select_email_query = """
SELECT
 *
FROM
  people
WHERE
  people.email = ?
"""
select_name_query = """
SELECT
 *
FROM
  people
WHERE
  people.name = ?
  AND
  people.surname = ?
"""

# UPDATE QUERY
update_query = """
UPDATE
  people
SET
  name = ?,
  surname = ?,
  email = ?,
  birthday = ?,
  nameday = ?,
  address = ?,
  interests = ?,
  phone = ?,
  socials = ?  
WHERE
  id = ?
"""

# CREATE TABLE QUERY
create_data_table = """
CREATE TABLE IF NOT EXISTS people (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  surname TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  birthday TEXT NOT NULL,
  nameday TEXT,
  address TEXT,
  interests TEXT,
  phone TEXT UNIQUE,
  socials TEXT
);
"""


def create_connection(path="enigma.db"):
    """Creates/Establishes connection to database."""
    connection = None
    try:
        connection = sqlite3.connect(path)
        # print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query, params=None):
    """Executes Write Query"""
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        # print("Query executed successfully")
        return True
    except Error as e:
        print(f"The error '{e}' occurred")
        return False


def execute_read_query(connection, query, params=None):
    """Executes Read Query"""
    cursor = connection.cursor()
    result = None
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


if __name__ == "__main__":
    # CONNECT TO/CREATE DATABASE
    connection = create_connection()
    # CREATE TABLE
    execute_query(connection, create_data_table)
