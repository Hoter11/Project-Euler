# -*- coding: utf-8 -*-
#
# author: Roc Granada Verdú
# All the problems on github: https://github.com/Hoter11/Project-Euler
#
#
# Largest palindrome product:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome(digits):
    current = 0
    top = 10**digits
    for i in range(1,top):
        for j in range(1,top):
            num = i*j
            if isPalindrome(num) and num > current: current = num
    return current

def isPalindrome(number):
    """This function checks if a number is a palindrome"""
    number = str(number) #[digit for digit in str(number)]
    length = len(number)
    for i in range(0,length/2):
        if number[i] != number[length-1-i]: return False
    return True

print largest_palindrome(3)
