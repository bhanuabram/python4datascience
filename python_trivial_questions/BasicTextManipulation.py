# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:44:32 2023

@author: 902544749
"""

# Convert comma separated list to a string
prog1 = input("Enter first language: ")
prog2 = input("Enter second language: ")
prog3 = input("Enter third language: ")

favorite_prog = [prog1, prog2, prog3]

print("What is your favorite programming language: ", ", ".join(favorite_prog))

# Capitalize the first letter of a string
def capitalize(String):
    return String.title()

get_string1 = "hallo"
get_string2 = "python ist einfach und macht spaß"
get_string3 = "die Apfelschorle ist zu süß"
get_string4 = "fünf sechs sieben acht"

print("The capitalized string for string 1 is: ", capitalize(get_string1))
print("The capitalized string for string 2 is: ", capitalize(get_string2))
print("The capitalized string for string 3 is: ", capitalize(get_string3))
print("The capitalized string for string 4 is: ", capitalize(get_string4))
