from select import select
import sqlite3
from tkinter.tix import MAX, Select

#check
print("sqlite3 imported successfully")

#create a database called celebs
conn = sqlite3.connect("celebs.db")

#check
print("Connection created successfully")

#create a cursor object
cursor = conn.cursor()

#check
print("cursor object created successfully")

#create a table called celebrity
# cursor.execute(
#     """
#     CREATE TABLE celebrity(
#         name TEXT,
#         genre TEXT,
#         num_albums INTEGER,
#         age INTEGER,
#         award INTEGER,
#         years_in_industry INTEGER
#     )
#     """
# )

#check
print("Table created successfully")

#insert values into your table
celebrity_info = [
                    ('Wizkid', 'Afrobeats', '4', '32', '76', '2001'),
                    ('Davido', 'Afrobeats', '3', '29', '34', '2011'),
                    ('BurnaBoy', 'Afrobeats', '6', '31', '47', '2012'),
                    ('Tiwa Savage', 'Afrobeats', '3', '42',	'20', '2010'),
                    ('Diamond Platnumz', 'Afropop', '3', '32', '28', '2006'),
                    ('2baba', 'Afrobeats', '9', '46', '50', '1996'),
                    ('Yemi Alade', 'R&B', '5', '33', '4', '2014'),
                    ('Shatta Wale', 'Dancehall', '6', '37', '11', '2004'),
                    ('Flavour',	 'Highlife', '6', '38',	'14', '2005'),
                    ('Phyno', 'Afropop', '3', '35', '5', '2003'),
                    ('Ice Prince', 'Afrobeats', '4', '35', '9', '1999'),
                    ('Sarkodie', 'Hip hop', '6', '37', '107', '2005'),
                    ('Zlatan', 'Afropop', '1', '27', '103', '2014'),
                    ('Daddy Lumba', 'Highlife',	'33', '57', '3', '1983'),
                    ('Olamide', 'Hip hop', '9', '33', '22', '2010'),
                    ('Samini', 'Dancehall',	'7', '40', '13', '1999'),
                    ('Ycee', 'Afrobeats', '1', '29', '2', '2012'),
                    ('Stonebwoy', 'Afropop', '4', '34', '28', '2012'),
                    ('Kcee', 'Afrobeats', '3', '43', '2', '2011'),
                    ('Banky W', 'Afrobeats', '7', '41', '7', '2002'),
                    ('Falz', 'Afropop',	'4', '31', '9', '2009')
                ]       
conn.commit()

#check
print("List created successfully")

cursor.executemany ("INSERT INTO celebrity VALUES(?, ?, ?, ?, ?, ?)", celebrity_info)

#check
print("celebrity info inserted successfully")

#print(celebrity_info) ;print(type(celebrity_info))

#commit connection
conn.commit()

#close connection
conn.close()


