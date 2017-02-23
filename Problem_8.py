# -*- coding: utf-8 -*-
#
# author: Roc Granada Verdú
# All the problems on github: https://github.com/Hoter11/Project-Euler

#The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.
#Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

def greatest_product(adjacents):
    """
    Preprocess: Get all the semi-series that doesnt contain a 0.

    For all semi-series, if it is larger than the adjecents wanted, check the
    best adjacent numbers.

    Return the best result.

    Notes: Even if we still have to do an iteration over all numbers to find
    the zeros, in the average case is faster than trying all possible combinations from the start.
    """

    series = []
    last = 0
    result = float("-inf")
    numer = 1

    for i,num in enumerate(number):
        if num == "0":
            series.append(number[last:i])
            last = i+1

    for serie in series:
        if len(serie) > adjacents:
            mult,aux = adjacent_product(serie,adjacents)
            if mult > result: result,numer = mult,aux

    return result,numer

def adjacent_product(serie,adjacents):
    result = float("-inf")
    num = 1
    #len(serie) - number of adjacents + 1 --> number of posible partitions
    for i in range(0,len(serie)-adjacents+1):
        mult = digits_multiplication(serie[i:(i+adjacents)])
        if mult > result: result,num = mult, serie[i:(i+adjacents)]
    return result,num

def digits_multiplication(serie):
    serie = [int(s) for s in list(serie)]

    result = 1
    for elem in serie:
        result *= elem
    return result


print greatest_product(13)
