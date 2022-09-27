
import mysql.connector
from mysql.connector import Error

def create_server_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database = db_name
        )
        print("MySQL Database connection was successful.")
    except Error as err:
        print(f"Error: '{err}'")

    return connection



def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully.")
    except Error as err:
        print(f"Error: '{err}'")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_new_table1 = """
create table Book_Information(
book_id int primary key,
title VARCHAR(20) NOT NULL,
genre VARCHAR(20) NOT NULL,
price VARCHAR(20) NOT NULL);
"""

create_new_table2 = """
create table Employee_Information(
employee_id int primary key,
name VARCHAR(20) NOT NULL,
position VARCHAR(20) NOT NULL,
schedule VARCHAR(20) NOT NULL,
benefits_status VARCHAR(20) NOT NULL);
"""

Book_Info = """
insert into Book_Information VALUES
(001, "Don Quixote", "Literature", "$25"),
(002, "Tom Clancy", "Novel", "$15"),
(003, "Harry Potter", "Novel", "$15"),
(004, "Lincoln", "Biography", "$20");
"""

Employee_Info = """
insert into Employee_Information VALUES
( 123, "John Berry", "Cashier", "M-F", "Enrolled"),
( 124 , "Mia Thompson", "Cashier", "Th-Sun", "Not Enrolled"),
( 125 , "Robert Rivera", "Supervisor", "Sat-Th", "Enrolled"),
( 126 , "Oscar Ramos", "General Manager", "All week", "Enrolled")


"""

#Callout section

connection = create_server_connection("localhost", "root", "student", "Bookstore")
execute_query(connection, Employee_Info)
