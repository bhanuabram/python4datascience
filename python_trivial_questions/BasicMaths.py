# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:06:08 2023

@author: 902544749
"""

import pandas as pd
import numpy as np
import math

print("Hello, Python! Let's do some basic maths!")

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = int(num1) + int(num2)
sub = int(num1) - int(num2)
mul = float(num1) * float(num2)
div = float(num1) / float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, sub))
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))
print('The division of {0} and {1} is {2}'.format(num1, num2, div))

num3 = input("Enter a number to check even/odd: ") 

# Check to see if num3 is even/odd
if (int(num1) % 2) == 0:
   print("{0} is an Odd number".format(num3))
else:  
   print("{0} is an Even number".format(num3))

# Check to see which of the numbers is the highest
maximum = max(int(num1), int(num2))
print("The maximum number is: ", maximum)

# Check if the number is a prime number or not
def PrimeChecking(num):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                print("The number", num, "is not a prime number")
                break
        else:
            print("The number", num, "is a prime number")
    else:
        print("The number", num, "is not a prime number")

PrimeChecking(int(num1))
PrimeChecking(int(num2))
PrimeChecking(int(num3))

# Find factorial of a given number
def factorial(num):
    return(math.factorial(num))

num4 = int(input('Please enter a number to find the factorial: '))
print("The factorial of the given number", num4, "is", factorial(num4))

# Calculate the square root of a given number
n = float(input('Enter a number to find square root: '))
n_sqrt = n ** 0.5

print("The square root of {0} is {1}".format(n, n_sqrt))

# Calculate the area of a triangle
s1 = float(input('Enter first side value: '))
s2 = float(input('Enter second side value: '))
s3 = float(input('Enter third side value: '))

sp = (s1 + s2 + s3) / 2
trianglearea = (sp * (sp - s1) * (sp - 2) * (sp - s3)) ** 0.5

print("The area of the triangle with sides {0}, {1}, {2} is equals to: {3}".format(s1, s2, s3, trianglearea))