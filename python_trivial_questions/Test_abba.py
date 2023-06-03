# -*- coding: utf-8 -*-
"""
Created on Thu May 18 22:40:27 2023

@author: 902544749
"""

def solution(A):
    A = [*A]
    for i in range(1, len(A)):
        if(A[i-1] == 'b' and A[i] == 'a'):
            return False
    return True

x = 'abba'
print(solution(x))