# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:39:29 2023

@author: 902544749
"""

# Find vowels from a string
def get_vowels(String):
    return [each for each in String if each in "aeiou"]

get_string1 = "hallo"
get_string2 = "python ist einfach und macht spaß"
get_string3 = "die Apfelschorle ist zu süß"
get_string4 = "1234fünfsechssieben"

print("The vowels for string 1 are ", get_vowels(get_string1))
print("The vowels for string 2 are ", get_vowels(get_string2))
print("The vowels for string 3 are ", get_vowels(get_string3))
print("The vowels for string 4 are ", get_vowels(get_string4))
