"""
(c)HAN University/Martijn van der Bruggen
Voorbeeld van recursie vs. iteratie aaan de hand
van het berekenen van de reeks van Fibonacci
Creatie d.d. 17 december 2018

"""

import timeit

def main():

    print ("Tijd in seconden iteratief")
    tijd = timeit.timeit("fibI(10)",setup="from __main__ import fibI")
    print (tijd)

    print ("Tijd in seconden recursief")
    tijd = timeit.timeit("fibR(10)",setup="from __main__ import fibR")
    print (tijd)


# The fib function returns the nth number
# in the Fibonacci series.
def fibR(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibR(n - 1) + fibR(n - 2)


# iteration
def fibI(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


# Call the main function.
main()