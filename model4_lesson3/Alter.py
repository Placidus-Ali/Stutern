import sqlite3

from colorama import Cursor

#check 
print("sqlite3 imported successfully")

#connect to database
conn = sqlite3.connect("Students.db")


# #check
print("Connection created successfully")

# #create cursor object
Cursor = conn.cursor()

#check
print("cursor object created successfully")

# #create a table called students_data
# Cursor.execute(
#     """
#     CREATE TABLE students_data(
#         first_name text,
#         last_name text,
#         email text,
#         course text
#     )
#     """
# )

# # #check
# print("table created successfully")

# conn.commit()

# #insert values into the table
students_list = [

                    ('Will', 'Johnson', 'willjohnson@stutern.com', 'data science'),
                    ('John', 'Smith', 'Johnsmith@stutern.com', 'data science'),
                    ('Katy', 'Brown', 'Katybrown@stutern.com', 'data science')
]

# #check
print("Info inserted successfully")

# Cursor.executemany("INSERT INTO students_data VALUES(?, ?, ?, ?)", students_list)

# conn.commit()

#check
print("Students data inserted successfully")

# #query the database
# Cursor.execute("SELECT * FROM students_data")

# items = Cursor.fetchall()
# print("First Name"+ "\t Last Name"+ "\t\t E-mail"+ "\t\t\t Course \n" f"{'.' * 100}" )

# # # Loop through the items
# for item in items:
#     first_name, last_name, email, course = item
#     print(f"{first_name:16}{last_name:20}{email:35}{course:20}")

# Alter table
# change the tabel name

# Cursor.execute ("ALTER TABLE students_data RENAME TO students_details")

# #check
# print("Table name changed")

#Alter column name(add new column)
# Cursor.execute("ALTER TABLE students_details ADD COLUMN level")

#check
print("New column added successfully")

#Add info to the new column
# Cursor.execute(
#     """
#     UPDATE students_details SET level = 'Beginner'
#     """
# )
# #check
# print("update done successfully")

conn.commit()

#query the database
Cursor.execute("SELECT * FROM students_details")

items = Cursor.fetchall()
print("First Name"+ "\t Last Name"+ "\t\t E-mail"+ "\t\t\t\t Course"+ "\t\t Level \n" f"{'.' * 100}" )

# Loop through the items
for item in items:
    first_name, last_name, email, course, level = item
    print(f"{first_name:16}{last_name:20}{email:32}{course:20}{level:18}")

conn.commit()

conn.close()
