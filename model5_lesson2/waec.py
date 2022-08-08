import sqlite3
import csv

#check
print("Sqlite3 and csv imported")

#create connection
conn = sqlite3.connect("waec_result.db")

#check 
print("connection created successfully")

#create a cursor object
cursor = conn.cursor()

#check
print("Cursor object created")

# #create a table called waec_data
table =  """CREATE TABLE waec_data(
        Name TEXT,
        English INTEGER,
        Maths INTEGER,
        Biology INTEGER,
        Chemistry INTEGER,
        Physics INTEGER,
        Agric INTEGER,
        Igbo INTEGER,
        Geography INTEGER,
        CRS INTEGER
            
    )
    """

#check
print("Table created successfully")

conn.commit()

cursor.execute(table)

# To read my csv file
with open('waec_result.csv') as opened_file:
    read_file = csv.reader(opened_file)
    
    #This command is used to skip header of a file
    next(opened_file)

    cursor.executemany(""" INSERT INTO waec_data VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", read_file)

#check
print("Executed")
