import math
def add(x, y):
    return x + y


def subtract(x, y):
    return x-y


def divide(x, y):
    if y == 0:
        print("Cannot divide by zero!")
    return x / y



def multiply(x, y):
    x*y


def square(x):
    return x**2


def power(x, y):
    return x**y


def sqrt(x):
    if x < 0:
       print("Square root of negative number is not real")
    else:    
    return math.sqrt(x)
    

