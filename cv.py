#!/usr/bin/env python

'''
Python program to convert a decimal number into binary, octal, and hexadecimal
number system(s)

Usage:
    Valid inputs are positive integer values [0-n]:

        $ python cv.py 20
'''

import sys

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "1.0.2"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"


def main():


    userInput = sys.argv[1]

    try:
        userInput = int(userInput)
    except:
        print "error: input must be numeric."
        exit(0)

    print "converted values of", userInput, '\n'

    data = [[bin(userInput), ": binary"], [oct(userInput), ": octal"], [hex(userInput), ": hexadecimal"]]
    col_width = max(len(word) for row in data for word in row) + 2
    for row in data:
        print "".join(word.ljust(col_width) for word in row)


if __name__ == "__main__":
    main()
