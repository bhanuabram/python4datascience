# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:11:20 2023

@author: 902544749
"""

def BinToDec(bnum):
    decnum = 0
    for i in range(len(bnum)):
        digit = int(bnum[i])
        decnum += digit * 2**(len(bnum)-i-1)
    return decnum

def solution(S):
    c = 0
    V = int(BinToDec(S))
    while(V != 0):
        if(V % 2 == 0):
            V = V // 2
            c += 1
        else:
            V -= 1
            c += 1
    return c

#binary = '10010110'
#print(BinToDec(binary))

V = '10010110'
print(solution(V))