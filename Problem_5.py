# -*- coding: utf-8 -*-
#
# author: Roc Granada Verdú
# All the problems on github: https://github.com/Hoter11/Project-Euler
#
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""Solution theory
Prime divisors of 2520 --> 5 * 2^3 * 3^2 * 7. With combinations of multiplying those numbers, you can get all numbers between 1 and 10.

So to get the smallest, first all the prime numbers must be multiplied:
2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
then all others numbers must be able to be reached of multiplications of those numbers.
20 -> 2 * 2 * 5
18 -> 2 * 3 * 3
16 -> 2 * 2 * 2 * 2
...

All we get is the maximum number of every prime number needed.
Solution: 5 * 2 * 2 * 2 * 2 * 3 * 3 * 7 * 11 * 13 * 17 * 19 = 232792560
"""

import math

def func(number):
    #extract all prime numbers
    primes = primes_func(number)
    #create dicc
    dicc = dicc_primes(primes)
    for num in range(1,number):
        factors = factorization(num)
        count = {}
        for factor in factors:
            try:
                count[factor] += 1
            except:
                count[factor] = 1
        for key in count.keys():
            if count[key] > dicc[key]:
                dicc[key] = count[key]

    result = 1
    for key in dicc.keys():
        result *= key**dicc[key]
    return result

def dicc_primes(primes):
    """Initalizes a diccionary with the ocurrences of every prime factor"""
    dicc = {}
    for prime in primes:
        dicc[prime] = 1
    return dicc

def primes_func(number):
    """Return all the prime numbers from 2 to the number specified
    Negative --> converted to positive
    Float --> converted to integer
    """
    if number == 1: return [1]
    primes = []
    number = int(abs(number))
    for i in range(2,number+1):
        is_prime = True
        for prime in primes:
            if i%prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    #print primes_divisors
    return primes

def factorization(n):
    """Return factorization of a number
    http://stackoverflow.com/questions/16996217/prime-factorization-list"""
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

print func(20)
