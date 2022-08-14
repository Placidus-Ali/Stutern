# create a list of integers between 5.5 and 20.5
list1 = [5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 17.5, 18, 18.5, 19, 19.5, 20]

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