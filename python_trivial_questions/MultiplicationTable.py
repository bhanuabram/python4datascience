# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:08:07 2023

@author: 902544749
"""

# Display a multiplication table using for loop
tab_number = int(input("Enter the number of your choice to print the multiplication table: "))

def MulTable(num):
    for count in range(1, 11):
        print(num, 'x', count, '=', num * count)

print("The multiplication table of: ", tab_number)
MulTable(tab_number)