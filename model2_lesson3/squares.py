"""
Write a python program to generate and print a dictionary containing keys ranging 
from 5 to 15 (with both numbers included) and the values are the squares of the keys.
"""

squares = {x: x*x for x in range(5,16)}
print(squares)