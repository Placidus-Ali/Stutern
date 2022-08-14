import sqlite3
import csv

#check
print("Sqlite3 and csv imported")

import csv

#create a connection
conn = sqlite3.connect("coursemate.db")

#check 
print("Connection created")

#create a cursor object
cursor = conn.cursor()

#check
print('Cursor object created')

# #create a table called coursemate
cursor.execute( """
CREATE TABLE coursemate(
        first_name TEXT,
        last_name TEXT,
        email TEXT,
        course TEXT,
        level TEXT
    )
   """)

#check
print("Table created")

conn.commit()

#insert values into your table
coursemate_info = [
            ('Abubakar', 'Adisa', 'adisaabubakar@gmail.com', 'Data Science', 'Beginner'), ('Adebisi', 'Afolabi', 'wasola.afolabi@yahoo.com', 'Data Science', 'Beginner'),
            ('Adedoyin', 'Abass', 'doyinabass0@gmail.com', 'Data Science', 'Beginner'), ('Awonaike', 'Tawakalitu', 'purpleduralumin@gmail.com' 'Data Science', 'Beginner'),
            ('Babajide', 'Adesugba', 'jide_ade@hotmail.com', 'Data Science', 'Beginner'), ('Bukola', 'Ajayi', 'bukolam.ajayi@gmail.com', 'Data Science', 'Beginner'),
            ('Binta', 'Umar', 'ubinta63@yahoo.com', 'Data Science', 'Beginner'), ('Christian', 'Uzondu', 'uzonduchristian2@gmail.com', 'Data Science', 'Beginner'),
            ('Cynthia', 'Awiya', 'awiyac@yahoo.com', 'Data Science', 'Beginner'), ('Deborah', 'Olorunnishola', 'deboraholuwatobi247@gmail.com', 'Data Science', 'Beginner'),
            ('Eke', 'Ihuoma', 'ihuomaeke28@gmail.com', 'Data Science', 'Beginner'), ('Esther', 'Akpanowo', 'estherakpanowo@gmail.com', 'Data Science', 	'Beginner'),
            (), (),
            (), (),
            (), (),
            (), (),


                    
                ]       
conn.commit()

#check
print("List created successfully")