"""
Create a class called car
Give 5 attributes of the car class
Give 5 methods of the car class
"""

class Car:
    #Give 5 attributes of the car class
    Color = "Red"
    Wheel = 4
    Seat = "Leather"
    Gear = 6
    Break = "Automatic"

    def __init__(self, Color, Wheel, Seat, Gear, Break):
        self.Color = Color
        self.Wheel = Wheel
        self.Seat = Seat
        self.Gear = Gear
        self.Break = Break


Benz = Car
print(Benz.Color)
print(Benz.Wheel)
print(Benz.Seat)
print(Benz.Gear)
print(Benz.Break)