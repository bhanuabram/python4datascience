# -*- coding: utf-8 -*-
"""
Created on Mon May 15 23:07:41 2023

@author: 902544749
"""

# Python Namespace Program Example

def outer_function():
    global num
    num = 20

    def inner_function():
        num = 30
        print('num =', num)

    inner_function()
    print('num =', num)


num = 10
outer_function()
print('num =', num)
