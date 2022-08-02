# Create a class called “Group_leader” that inherits from the class “Students”
# creating parent class Student


class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com' 

stud_1 = Student('Jame', 'Anam')
stud_2 = Student('Precious', 'Jane')

#create 3 more instance of the parent class
stud_3 = Student('Lucky', 'Tobi')
stud_4 = Student('Dare', 'Peace')
stud_5 = Student('Temi', 'Lois')

#creating a child class (Group_leader)
class Group_leader(Student):
    def __init__(self, first, last, Student = []):
        self.first = first
        self.last = last

#Define a method that prints out the full names of students in the list of students under group leader
    def full_name(self):
        print('{} {}'.format(Group_leader_1.first, Group_leader_1.last))
        print('{} {}'.format(Group_leader_2.first, Group_leader_2.last))


#Create 2 instances of the sub class
Group_leader_1 = Student('Placidus', 'Ebuka')
Group_leader_2 = Student('Ani', 'Lawrence')
    
print(Group_leader_1.first)

#Print the fullname of the students in the list of students under the instances of your subclass
print('{} {}'.format(Group_leader_1.first, Group_leader_1.last))
print('{} {}'.format(Group_leader_2.first, Group_leader_2.last))

#Print the email of the instances of your subclass
print(Group_leader_1.email)
print(Group_leader_2.email)
