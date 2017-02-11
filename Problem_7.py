# -*- coding: utf-8 -*-
#
# author: Roc Granada Verdú
# All the problems on github: https://github.com/Hoter11/Project-Euler

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?


def primes_func(number):
    """Return all the prime numbers from 2 to the number specified
    Negative --> converted to positive
    Float --> converted to integer
    """
    if number == 1: return [1]
    primes = []
    number = int(abs(number))
    i = 2
    done = False
    len = 0
    while not done:
        is_prime = True
        for prime in primes:
            if i%prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            len += 1
        i += 1
        if len >= number:
            done = True

    #print primes_divisors
    return primes[-1]

print primes_func(10001)
