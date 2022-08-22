import pandas as pd
import matplotlib 
from matplotlib import pyplot as plt
import csv

# #load and read existing file
df = pd.read_csv('company_sales_data.csv')

#check
print("csv file read")

x = df(month_number)
y = df(facecream, facewash,toothpaste,bathingsoap,shampoo,maoisturizer)

plt.plot(month_number,facecream, color= 'olive', linestyle= '--', marker= "o")
plt.plot(month_number,facewash, color= 'black', linestyle= '--', marker= "d")
plt.plot(month_number,toothpaste, color= 'blue', linestyle= ':', marker= "o")
plt.plot(month_number,bathingsoap, color= 'purple', linestyle= '-', marker= "X")
plt.plot(month_number,shampoo, color= 'indigo', linestyle= ':', marker= "o")
plt.plot(month_number,moisturizer, color= 'red', linestyle= '', marker= "o")
plt.title("A Multiple Line Graph Of Months Against Product Sales")
plt.xlabel("Months Of The Year In Numbers")
plt.ylabel("Amount Of Sales From Products")
plt.legend(["facecream","facewash","toothpaste","bathingsoap","shampoo","moisturizer"], loc='upper left')
plt.show()