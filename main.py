# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:01:24 2023

@author: Barış
"""

x = int(input("Number: \n"))

y = 2, 3, 5, 7


primes = []
for a in range(len(y)):
    if x == y[a]:
        primes = [True, True, True, True]
        break
    
    if int(x/y[a])*y[a] != x:
        primes.append(True)

if len(primes) == 4:
    print("This number is a prime")
else:
    print("This number isn't a prime")