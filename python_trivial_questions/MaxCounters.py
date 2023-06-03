# -*- coding: utf-8 -*-
"""
Created on Thu May 18 00:55:11 2023

@author: 902544749
"""

# MaxCounters
# You are given N counters, initially set to 0, and you have two possible
# operations on them:
# increase(X) − counter X is increased by 1,
# max counter − all counters are set to the maximum value of any counter.
# A non-empty array A of M integers is given. This array represents consecutive
# operations:

# if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
# if A[K] = N + 1 then operation K is max counter.
# For example, given integer N = 5 and array A such that:
#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the values of the counters after each consecutive operation will be:
#     (0, 0, 1, 0, 0)
#     (0, 0, 1, 1, 0)
#     (0, 0, 1, 2, 0)
#     (2, 2, 2, 2, 2)
#     (3, 2, 2, 2, 2)
#     (3, 2, 2, 3, 2)
#     (3, 2, 2, 4, 2)
# The goal is to calculate the value of every counter after all operations.

# Write a function:
# def solution(N, A)
# that, given an integer N and a non-empty array A consisting of M integers,
# returns a sequence of integers representing the values of the counters.

# Result array should be returned as an array of integers.
# For example, given:
#     A[0] = 3
#     A[1] = 4
#     A[2] = 4
#     A[3] = 6
#     A[4] = 1
#     A[5] = 4
#     A[6] = 4
# the function should return [3, 2, 2, 4, 2], as explained above.

# Write an efficient algorithm for the following assumptions:
# N and M are integers within the range [1..100,000];
# each element of array A is an integer within the range [1..N + 1].

def solution(N, A):
    r = [0] * N
    m = []
    l = len(A) - 1
    
    for i in range(0, len(A)):
        if(0 < A[i] < l):
            r[A[i]-1] += 1
            m = r
        else:
            for j in range(0, len(r)):
                r[j-1] = max(m)

    return r

N = 5
A = [3, 4, 4, 6, 1, 4, 4]
print(solution(N, A))

# N = 5
# A = [3, 4, 4, 6, 1, 4, 4]
# array n contains 5 integers starting from 0

# 3	-->		(0, 0, 1, 0, 0)		K = Increase A[3]
# 4	-->		(0, 0, 1, 1, 0)		K = Increase A[4]
# 4	-->		(0, 0, 1, 2, 0)		K = Increase A[3]
# 6	-->		(2, 2, 2, 2, 2)		K = Set n[0:n] = max(A)
# 1	-->		(3, 2, 2, 2, 2)		K = Increase A[1]
# 4	-->		(3, 2, 2, 3, 2)		K = Increase A[4]
# 4	-->		(3, 2, 2, 4, 2)		K = Increase A[4]
