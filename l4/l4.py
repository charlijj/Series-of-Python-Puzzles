# CSCI 331 - Lab 4
# Author: Jasper Charlinski
# Date: Mar 15th, 2023

"""
This program extends the abstract base class UserList class. Python's collections module has some concrete classes that derive from abstract base classes; these
can, of course, be further derived.

More specifically extending the methods in the Lab4 class. The methods must directly change the the object, and not make a copy
of it.

Example output:

Test 0 - initial state:
[43, 44, 51, 47]
Test 1 - repeat(4):
[43, 44, 51, 47, 43, 44, 51, 47, 43, 44, 51, 47, 43, 44, 51, 47]
Test 2 - add(70) - add(31):
[43, 44, 51, 47, 43, 44, 51, 47, 43, 44, 51, 47, 43, 44, 51, 47, 70, 31]
Test 3 - remove(5, 8):
[43, 44, 51, 47, 43, 44, 51, 47, 43, 44, 51, 47, 70, 31]
Test 4 - concat([48, 91, 46]):
[43, 44, 51, 47, 43, 44, 51, 47, 43, 44, 51, 47, 70, 31, 48, 91, 46]
Test 5 - depth():
[43, 44, 51, 47, 43, 44, 51, 47, 43, 44, 51, 47, 70, 31, 48, 91, 46, [93, 8], [[70], 50]]
depth: 2
Elapsed time is 0.000126 seconds.

In this example the original list is [43, 44, 51, 47], which is then repetend 4 times, then 70 and 31 are appended to the end of the list, 
then the items in the index range of 5 - 8 are removed from the list, then [48, 91, 46] is appended to the end of the list,
then [93, 8] and [[70], 50] are appended to the list and the max depth of all internal lists is calculated and returned, in this case it is 2 with [[70], 50].  
"""

from collections import UserList
from pytictoc import TicToc
import sys
import random


class Lab4(UserList):

    def repeat(self, n: int) -> None:
    # Repeat the existing object n times.

        origList = self.copy() # get copy of original list 

        for i in range(n):

            super().extend(origList) # append the original list to itself n times


    def add(self, x) -> None:
    # Adds x to the end of the object.

        super().append(x)


    def remove(self, m: int , n: int) -> None:
    # Removes all elements between indices m and n (inclusive) in the object.
        
        del self[m:n+1] # delete all items in self that are in the range of m - n (including m and n)


    def concat(self, x: list) -> None:
    # Concatenates the object with x (which can be another object derived from a UserList class).
        
        super().extend(x)


    def depth(self, l) -> int:
    # Assuming that the object contains other nested objects, Should return the depth of the deepest UserList.

        if isinstance(l, int):  # base case: depth of an int is 0
            return 0

        else:
            maxDepth = 1 # initial max depth is 1

            for item in l:

                # add 'or isinstance(item, list)' to include regular lists in max depth calculation 
                if isinstance(item, UserList) : # if item is a UserList, ie there is another layer of nesting

                    maxDepth = self.depth(item) + 1  # recursively calculate depth of nested list

            return maxDepth


if __name__ == '__main__':
    #DO NOT MODIFY THIS CODE

    R1 = 0
    R2 = 100

    t = TicToc()
    t.tic() # start timer

    l4 = Lab4([random.randint(R1, R2) for r in range(4)])

    print('Test 0 - initial state:')
    print(l4)

    print('Test 1 - repeat():')
    l4.repeat(2)
    print(l4)

    print('Test 2 - add():')
    l4.add(random.randint(R1, R2))
    l4.add(random.randint(R1, R2))
    print(l4)

    print('Test 3 - remove():')
    l4.remove(5,8)
    print(l4)

    print('Test 4 - concat():')
    l4.concat( Lab4([random.randint(R1, R2) for r in range(3)]) )
    print(l4)

    print('Test 5 - depth():')
    l4.add( Lab4([random.randint(R1, R2) for r in range(2)]) )
    n1 = random.randint(R1, R2)
    l4.add( Lab4([ Lab4([ random.randint(R1, R2) for r in range(1)]) , n1]) )
    print(l4)
    print('depth:', l4.depth(l4.data))

    t.toc() #elapsed time
    print('*' * 13)
