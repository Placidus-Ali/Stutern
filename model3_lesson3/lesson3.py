# Create a class called “Group_leader” that inherits from the class “Students”
# creating parent class Student
class Student:
    

#creating a child class (Group_leader)
class Group_leader(Student):
    def __init__(self, first, last, student= None):
        self.first = first
        self.last = last
        
    Group_leader_1 = Group_leader('Placidus', 'Ebuka')
    Group_leader_2 = Group_leader('Ani', 'Lawrence')
    