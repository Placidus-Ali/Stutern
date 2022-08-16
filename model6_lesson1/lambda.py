# create a list of integers between 5.5 and 20.5
list1 = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

#Lambda function to count even numbers in the list
count_even_num = list(filter(lambda x: (x%2 == 0), list1))
print(count_even_num)

#Lambda function to count odd numbers in the list
count_odd_num = list(filter(lambda x: (x%2 != 0), list1))
print(count_odd_num)

#Lambda function to sqaure all the numbers in the list
square_num = list(map(lambda x: x**2, list1))
print(square_num)

#Lambda function to cube all the numbers in the list
cube_num = list(map(lambda x: x**3, list1))
print(cube_num)