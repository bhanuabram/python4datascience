# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:18:28 2023

@author: 902544749
"""

fib_nums = [0, 1]

number = int(input("Enter the number you want to check for fibonacci number: "))

while fib_nums[-1] <= number:
    fib_nums.append(fib_nums[-1] + fib_nums[-2])

if number in fib_nums:
    print(f'Yes. {number} is a fibonacci number.')
else:
    print(f'No. {number} is not a fibonacci number')