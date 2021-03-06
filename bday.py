#!/usr/bin/env python

'''
Python program to simulate the birthday problem or birthday paradox to determine if
the probability that, in a set of (n) randomly chosen people, some pair of them will
have the same birthday.

Usage:
    Valid inputs are positive integer values:

        $ python bday.py 23
'''

import random
import sys

__author__ = "M. Jastad"
__copyright__ = "Copyright(c) 2015"
__license__ = "USE-AS-IS"
__version__ = "1.1.5"
__maintainer__ = "M. Jastad"
__email__ = "majastad@icloud.com"


def has_duplicates(listToCheck):
    number_set = set(listToCheck)

    if len(number_set) is not len(listToCheck) : return True
    else : return False

def main():

   
    if len(sys.argv) < 2 : exit(0)

    duplicateNumber = 0

    userInput = sys.argv[1]

    try:
        userInput = int(userInput)
    except:
        print "error: ", userInput, "is non-numeric."
        exit(0)

    if userInput <= 0:
        print("error: enter a positive integer")
        exit(0)

    for i in range(0,1000):
        birthdayList = []

        for j in range(0,userInput):
            birthday=random.randint(1,365)
            birthdayList.append(birthday)

        x = has_duplicates(birthdayList)

        if x : duplicateNumber += 1

    print "result: post 1000 simulations with " + str(userInput) + " student(s) there were: ", duplicateNumber,\
                    "simulations with at least one match.\n\tapproximate probability is: ", \
                    round(((duplicateNumber/1000.0)*100),3),"%"


if __name__ == "__main__":
    main()
