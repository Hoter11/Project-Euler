# -*- coding: utf-8 -*-
#
# author: Roc Granada Verdú
# All the problems on github: https://github.com/Hoter11/Project-Euler
#
#
#The sum of the squares of the first ten natural numbers is,
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural #numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred #natural numbers and the square of the sum.

def func(num):
    suma = 0
    resta = 0
    for i in range(1,num+1):
        suma += i**2
        resta += i

    return (resta**2 - suma)

import time
t1 = time.clock()
print func(1000000000)
t2 = time.clock()
print "Time: ", t2-t1
