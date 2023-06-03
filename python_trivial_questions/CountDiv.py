# -*- coding: utf-8 -*-
"""
Created on Thu May 18 12:19:43 2023

@author: 902544749
"""

# CountDiv
# Write a function:
# def solution(A, B, K)
# that, given three integers A, B and K, returns the number of integers within
# the range [A..B] that are divisible by K, i.e.:
# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3,
# because there are three numbers divisible by 2 within the range [6..11],
# namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

def solution(A, B, K):
    M = 0
    arr = []
    for i in range(A, B+1):
        arr.append(i)
    for i in range(0, len(arr)):
        if(arr[i] % K == 0):
            M += 1
    
    return M

A = 6
B = 11
K = 2

print(solution(A, B, K))