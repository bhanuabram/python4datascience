# -*- coding: utf-8 -*-
"""
Created on Wed May 17 19:26:57 2023

@author: 902544749
"""

# PermMissingElem
# An array A consisting of N different integers is given. The array contains
# integers in the range [1..(N + 1)], which means that exactly one element is
# missing. Your goal is to find that missing element.

# Write a function:
# def solution(A)
# that, given an array A, returns the value of the missing element.

# For example, given array A such that:
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

def solution(A):
    if(len(A) == 0):
        return 1
    elif(max(A) == len(A)):
        return len(A) + 1
    
    A.sort()
    for i in range(1, len(A) + 1):
        if i != A[i-1]:
            return i

A = [2, 3, 1, 5]
print(solution(A))

# A: 2, 3, 1, 5
# sort
# A: 1, 2, 3, 5
# i: 1, 2, 3, 4
#    y  y  y  * --> at this point, 4 != 5, hence return 4