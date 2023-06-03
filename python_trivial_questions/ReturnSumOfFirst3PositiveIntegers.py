# -*- coding: utf-8 -*-
"""
Created on Thu May 18 22:52:57 2023

@author: 902544749
"""

# ReturnsPositiveInteger
def solution(A):
    p = []
    c = 0
    for i in range(0, len(A)):
        if(A[i] > 0):
            p.append(A[i])
            c += 1
            if(c == 3 or i == len(A)):
                return sum(p)
    return sum(p)

A = [4, -2, 0, 5, -2, 1, 6]
B = [3, -2, 0]
C = [-9, -4, -2, -6]
print(solution(A))
print(solution(B))
print(solution(C))