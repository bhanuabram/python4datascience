# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:03:24 2023

@author: 902544749
"""

# Function to check leap year
def LeapYear(Year):
    if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
        print("The given Year is a leap year")
    else:
        print("The given Year is not a leap year")

year = int(input("Enter the year to check whether a leap year or not: "))
LeapYear(year)