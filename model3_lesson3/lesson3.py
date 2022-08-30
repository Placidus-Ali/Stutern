# Create a class called “Group_leader” that inherits from the class “Students”

# creating parent class Student
class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + "@gmail.com"

#check
print('Parent class and attributes created')

stud_1 = Student('Jane', 'Anam')
stud_2 = Student('Precious', 'Jane')

#create 3 more instance of the parent class
stud_3 = Student('Lucky', 'Tobi')
stud_4 = Student('Dare', 'Peace')
stud_5 = Student('Temi', 'Lois')

#check
print('Instances of Parent class created')

#creating a child class (Group_leader)
class Group_leader(Student):
    def __init__(self, first, last, student= []):

        # defining attributes of the method

        super().__init__(first, last)
        self.student = student

        if student is []:
            self.student = []
            print(self.student)

    # defining method that adds students 
    def add_student(self, add_new_student):
        self.student.append(add_new_student)
        print(self.student)

    # defining method that removes students

    def remove_student(self, remove_old_student):
        self.student.remove(remove_old_student)
        print(self.student)

    def __str__(self):
        return str(self.student)

    #check
    print('Parent class and attributes created')

#Create 2 instances of the sub class
Group_leader_1 = Group_leader('Placidus', 'Ebuka')
Group_leader_2 = Group_leader('Ani', 'Lawrence')

#Define a method that prints out the full names of students in the list of students under group leader
def full_name():
    print('{} {}'.format(Group_leader_1.first, Group_leader_1.last))
    print('{} {}'.format(Group_leader_2.first, Group_leader_2.last))

full_name()
#check
print('Method to print fulll name created')

# creating the 2 new students to Group_leader_1
stud_6 = ('Samson', 'John')
stud_7 = ("Amadi", "James")

# creating the 2 new students to Group_leader_2
stud_8 = ('Blessing', 'Mary')
stud_9 = ("Ebuka", "King")

# adding 2 students to ecah of the instance of the subclass
Group_leader_1.add_student(stud_6)
Group_leader_1.add_student(stud_7)
Group_leader_2.add_student(stud_8)
Group_leader_2.add_student(stud_9)

# removing one student from each of the instances of the subclass
Group_leader_1.remove_student(stud_6)
Group_leader_2.remove_student(stud_8)
    
print(Group_leader_1.first)

#Print the fullname of the students in the list of students under the instances of your subclass
print('{} {}'.format(Group_leader_1.first, Group_leader_1.last))
print('{} {}'.format(Group_leader_2.first, Group_leader_2.last))

#Print the email of the instances of your subclass
print(Group_leader_1.email)
print(Group_leader_2.email)
