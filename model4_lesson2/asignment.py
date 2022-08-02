# Create a SGA_1_3_learners database
import sqlite3

# Confirm that sqlite3 is imported successful
print("Successfully Imported Module")

# create or connect to a database
conn = sqlite3.connect("SGA_1_3_learners.db")

# check that connection is successful
print("SGA_1_3_learners Database created successfully!") ; print(type(conn))

# create a cursor object
cursor = conn.cursor()

# check that cursor object is created successfully
print("cursor object created successfully!")

# #create a table called learners with 4 columns
# cursor.execute("""
#                 CREATE TABLE learners (
#                     firt_name text,
#                     last_name text,
#                     email text,
#                     course text
#                 ) 
# """)

#check that table is created successfully
print("Table created successfully!")

#insert info into the table called learners
cursor.execute(
    """
    INSERT INTO learners
    VALUES  ('Abubakar', 'Adisa', 'adisaabubakar@gmail.com', 'Data Science'), ('Adebisi', 'Afolabi', 'wasola.afolabi@yahoo.com', 'Data Science'), 
            ('Adedoyin', 'Abass', 'doyinabass0@gmail.com', 'Data Science'), ('Awonaike', 'Tawakalitu', 'purpleduralumin@gmail.com', 'Data Science'), 
            ('Babajide', 'Adesugba', 'jide_ade@hotmail.com', 'Data Science'), ('Bukola', 'Ajayi', 'bukolam.ajayi@gmail.com', 'Data Science'), 
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
    """)

#check
print("Table inserted successfully")

#query data
cursor.execute(
    """
    SELECT * FROM learners
    """
    )

items = cursor.fetchall()

# format output to display in a tabular form
print("First_name"+ "\t Last_name"+ "\t\t Email:"+ "\t\t\t\t Course \n" f"{'.' * 100}" )

# Loop through the items
for item in items:
    first_name, last_name, email, course = item
    print(f"{first_name:16}{last_name:16}{email:35}{course}")


#check
print("Query executed successfully")
