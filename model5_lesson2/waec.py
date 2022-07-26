import sqlite3
import csv

#create a connection
conn = sqlite3.connect("waec_result.db")

#check 
print("Connection created")

#create a cursor object
cursor = conn.cursor()

#check
print('Cursor object created')

# #create a table called waec_result
create_table = """
CREATE TABLE waec_result(
        name TEXT,
        english INTEGER,
        maths INTEGER,
        biology INTEGER,
        chemistry INTEGER,
        physics INTEGER,
        agric INTEGER,
        igbo INTEGER,
        geography INTEGER,
        crs INTEGER
    )
   """

#check
print("Table created")

conn.commit()


cursor.execute(create_table)

#check
print("Cursor Executed successfully")


# #load existing table
with open('waecresult.csv', 'r') as file:
    read_file = csv.reader(file)

    #This command is used to skip header
    next(file)

    cursor.executemany(
        """INSERT INTO waec_result
         VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
         """, 
         read_file)

#check
print("data loaded into the table successfully")

conn.commit()

conn.close()

