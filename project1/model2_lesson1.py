# Define a function that returns the maximum of any three numbers a user inputs. Assign the result to a variable “max_num”
def max_num(x, y, z):
    if y <= x >= z:
        return x
    elif x <= y >= z:
        return y
    else:
        return z

m = max_num((int(input)), int((input)), int((input)))
print("The max_num is" , m)

