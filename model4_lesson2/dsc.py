# Create a SGA_1_3_learners database
import sqlite3

from colorama import Cursor

# Confirm that sqlite3 is imported successful
print("Successfully Imported Module")

# create or connect to a database
conn = sqlite3.connect("SGA_1_3_DSC")

# check that connection is successful
print("SGA_1_3_DSC Database created successfully!") ; print(type(conn))

# create a cursor object
Cursor = conn.cursor()

# check that cursor object is created successfully
print("Cursor object created successfully!")

# #create a table called Data_Science with 4 columns
# Cursor.execute("""
#                 CREATE TABLE Data_Science (
#                     firt_name text,
#                     last_name text,
#                     email text,
#                     course text
#                 ) 
# """)

#check that table is created successfully
print("Table created successfully!")

#create a row to input into the table called Data_Science
coursemate_list = [  
                     ('Abubakar', 'Adisa', 'adisaabubakar@gmail.com', 'Data Science'), ('Adebisi', 'Afolabi', 'wasola.afolabi@yahoo.com', 'Data Science'), 
                     ('Adedoyin', 'Abass', 'doyinabass0@gmail.com', 'Data Science'), ('Awonaike', 'Tawakalitu', 'purpleduralumin@gmail.com', 'Data Science'), 
                     ('Babajide', 'Adesugba' 'jide_ade@hotmail.com', 'Data Science'), ('Bukola', 'Ajayi', 'bukolam.ajayi@gmail.com', 'Data Science'), 
                     ('Binta', 'Umar', 'ubinta63@yahoo.com', 'Data Science'), ('Christian', 'Uzondu', 'uzonduchristian2@gmail.com', 'Data Science'),
                     ('Cynthia', 'Awiya', 'awiyac@yahoo.com', 'Data Science'), ('Deborah', 'Olorunnishola', 'deboraholuwatobi247@gmail.com', 'Data Science'),
                     ('Eke', 'Ihuoma', 'ihuomaeke28@gmail.com', 'Data Science'), ('Esther', 'Akpanowo', 'estherakpanowo@gmail.com', 'Data Science'), 
                     ('Eniola', 'Osadare', 'dorcasosadare@gmail.com', 'Data Science'), ('Etariemi', 'Louis', 'etariemilouis@gmail.com', 'Data Science'),
                     ('Faith', 'Amure', 'amuretalodabif@gmail.com', 'Data Science'), ('Ganiyat', 'Shittu', 'ganiyatas@gmail.com', 'Data Science'), 
                     ('Gideon', 'Uko', 'ukogideon13@gmail.com', 'Data Science'), ('Idowu', 'Adesanya', 'idsworld22@yahoo.com', 'Data Science'), 
                     ('Joyce', 'Ezeonwu', 'joyceokore@gmail.com', 'Data Science'), ('Kehinde', 'Orolade', 'kehindeorolade@gmail.com', 'Data Science'),
                     ('Kafayat', 'Ibrahim', 'kafayatadenike10@gmail.com', 'Data Science'), ('Lawrence', 'Aneshimokha', 'anelawrence1@gmail.com', 'Data Science'),
                     ('Mariam', 'Adeoti', 'adetutuadebola28@gmail.com', 'Data Science'), ('Ogechi', 'Njemanze', 'ogenjemz@gmail.com', 'Data Science'),
                     ('Omowunmi', 'Awonirana', 'mowunmi11@gmail.com', 'Data Science'), ('Placidus', 'Ali', 'Placidusali@gmail.com', 'Data Science'),
                     ('Praise', 'Emmanuel', 'praiseemmanuel9ic@gmail.com', 'Data Science'), ('Prince', 'Ekeocha', 'prince.ekeocha@gmail.com', 'Data Science'),
                     ('Rasheedat', 'Sikiru', 'rasheedatsikiru@gmail.com', 'Data Science'), ('Ramotallah', 'Jubril', 'jubrilramotallah03@gmail.com', 'Data Science'),
                     ('Sheriiff', 'Azeez', 'SheriffOlaitan71@gmail.com', 'Data Science'), ('Stephen', 'Ogungbile', 'stephenfunso@gmail.com', 'Data Science'), 
                     ('Temitope', 'Bamidele', 'bamideletemitope42@gmail.com', 'Data Science'), ('Theresa', 'Karamor', 'teriekarie@gmail.com', 'Data Science'), 
                     ('Tina', 'Uyateide', 'tinauyats@gmail.com', 'Data Science'), ('Victoria', 'Chukwuno', 'Chukwunovictoria@gmail.com', 'Data Science')
                     ]

#check
print("coursemates list create successfully")

#insert into info into the table
Cursor.executemany("""INSERT INTO Data_Science VALUES ( ?, ?, ?, ?)""", coursemate_list)

#check
print("Multpile info inserted successfully")
