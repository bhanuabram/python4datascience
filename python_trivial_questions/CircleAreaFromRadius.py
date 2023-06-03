# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:31:47 2023

@author: 902544749
"""

import math

# Find area of a circle based on a radius
def CircleArea(rad):
    return math.pi * (rad * rad)

rad = float(input("Enter the radius of the circle: "))
print("Area of the circle is %.6f" % CircleArea(rad))
