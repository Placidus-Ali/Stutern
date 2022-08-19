import sqlite3
import csv

#create a connection
conn = sqlite3.connect("waec_result.db")

#check 
print("Connection created")

#create a cursor object
cursor = conn.cursor()

items = cursor.fetchall()
#check
print("Cursor object created")

# Which student scored the highest in maths
#looping through the items
for item in items:
    name, english, maths,  biology, chemistry, physics, agric, igbo, geography, crs  = item

#The student with highest score in Maths
def highest_score_in_maths():
    cursor.execute ("""
    SELECT Name, 
    MAX(maths) FROM waec_result
    """)
    item = cursor.fetchall()
    print(f"Student with the highest Math score is, {item}")

#student with lowest score in english
def lowest_score_in_english():
    cursor.execute ("""
    SELECT Name, 
    MIN(english) FROM waec_result
    """) 
    item = cursor.fetchall()
    print(f"Student with the lowest English score is, {item}")

#Average score of students in Maths
def Average_student_score_in_maths():
    cursor.execute ("""
    SELECT 
    AVG(maths) FROM waec_result
    """) 
    item = cursor.fetchall()
    print(f"Average students score in maths is, {item}")

#Average score of students in English
def Average_student_score_in_english():
    cursor.execute ("""
     SELECT 
     AVG(english) FROM waec_result
     """)
    item = cursor.fetchall() 
    print(f"Average students score in English is, {item}")

#Who is the best performing student across all nine subjects in terms of overall scores
def best_overall_student():
     cursor.execute (""" 
     SELECT Name, 
     SUM(english + maths + biology + chemistry + physics + agric + igbo + geography + crs) 
     FROM waec_result
     """)
     item = cursor.fetchall()
     print(f"The best overall Student is, {item}")

#Who is the best performing student across all nine subjects in term of average scores
def best_student_on_average():
     cursor.execute (""" 
     SELECT Name, 
     AVG(english + maths + biology + chemistry + physics + agric + igbo + geography + crs) 
     FROM waec_result
     """)
     item = cursor.fetchall()
     print(f"The best overall Student on average is, {item}")

#calling my functions
highest_score_in_maths()
lowest_score_in_english()
Average_student_score_in_maths()
Average_student_score_in_english()
best_overall_student()
best_student_on_average()

conn.commit()

conn.close()
