# -*- coding: utf-8 -*-
#
# author: Roc Granada Verdú
# All the problems on github: https://github.com/Hoter11/Project-Euler
#
# NOTE: I'm not happy at all with this solution, however it works.
# It takes an average time of 114s to find the solution. This is a lot! (isn't it?)
# Maybe i'm gonna try for a more efficent solution in the future.
#
# Largest Prime Factor:
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
from itertools import islice, count
import math, time

def func(number):
    primes = [2]
    primes_divisors = []
    for i in range(3, int(math.sqrt(number)) - 1):
        found = False
        for prime in primes:
            if i % prime == 0:
                found = True
                break
        if not found:
            primes.append(i)
            if number % i == 0: primes_divisors.append(i)
    #print primes_divisors
    return primes_divisors[-1]

t1 = time.clock()
print func(600851475143)
t2 = time.clock()
print t2-t1
