#!/usr/bin/env python

'''
Python program to display the Fibonacci sequence up to n-th term using recursive functions

Usage:
    Valid inputs are positive integer values:

        $ python fib.py 10
'''

import sys

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "2.0.4"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))


def main():

    if len(sys.argv) < 2 : exit(0)
    userInput = sys.argv[1]

    try:
        userInput = int(userInput)
    except:
        print "error: ", userInput, "is non-numeric."
        exit(0)

    if userInput <= 0:
        print("error: enter a positive integer")
        exit(0)
    else:
        print("Fibonacci sequence:")
        for i in range(userInput):
            print(fibonacci(i))

if __name__ == "__main__":
    main()
