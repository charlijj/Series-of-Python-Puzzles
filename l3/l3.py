# CSCI 331 - Lab 3
# Author: Jasper Charlinski
# Due Date: Feb 22, 2023

"""

This is a program that creates a concordance by parsing given text files (in this case the text files are from Project Gutenberg), and extends
the Python class dict. A concordance is a list of the words present in a text, along with the line numbers in which they are found. 
It also returns each key value that has a length over 100, meaning that word is in the txt file more than 100 times.

Ex.) 

1232.txt produces:

***** Sample entries: *****
addresses [5149] -> the word 'addresses' appears on line 5149

Sforza [172, 384, 560, 643, 1191, 1201, 1404, 1918, 1921, 1932, 2003, 2190, 3088, 3089, 3108, 3108, 3115, 3350]
Second [162, 1360, 1387, 2050, 2348, 3514]
Service [5109]
neglected [2446, 3427, 4311]
possession [778, 873, 969, 1444, 1753, 2911, 3016, 3420, 4313, 4398, 4408, 4427, 4575, 4873]
contemptible [2646, 2657, 2923]
deceits [2562]
histories [2049, 2243]
However [4964]
***** Top Keys: *****
people 115 -> the word people appears 115 times 
prince 185
Castruccio 140

"""

from nltk.tokenize import wordpunct_tokenize
from pytictoc import TicToc
import sys
import random

class Lab3(dict):

    def __setitem__(self, key, value) -> None:
        
        if key in super().keys(): # If the give key already exists inside the dictionary 

            keyValue = super().get(key) # get the list associated with the key

            super().__setitem__(key, keyValue + [value]) # append the given value to the list associated with the key

        else: # else if it is the first appearance of the key

            super().__setitem__(key, [value]) # create a new key value pair

    def clear(self) -> None:

        print('*+* Erasing data ... *+*')
        super().clear()

    def topKeys(self, number: int = 100) -> list:

        topKeys = [] # list of each key with a list length greater than the specified number

        for key in super().keys(): # for each key in the dictionary

            numValues = len(super().get(key)) # get the length of the associated list

            if numValues >= number: 

                topKeys += [key] # this key has a associated list that is longer than the specified number, so add it to top keys list. 

        return topKeys      

if __name__ == '__main__':
    #DO NOT MODIFY THIS CODE
    t = TicToc()
    t.tic() # start timer
    
    NCHAR = 5
    CHOICES = 10
    STOPWORDSFILE = 'txts/stopwords.txt'

    try:
        f = open(STOPWORDSFILE, 'r')
    except OSError:
        print('ERROR: cannot open', STOPWORDSFILE)
    else:
        stopWords = [line.strip() for line in f.readlines()]
        f.close()

    try:
        fn = sys.argv[1]
        f = open(fn, 'r')
    except OSError:
        print('ERROR: cannot open', fn)
    else:
        al = [wordpunct_tokenize(line) for line in f.readlines()]
        f.close()    

        if al:
            lab3 = Lab3()

            for counter, line in enumerate(al):
                for item in line:
                    if item not in stopWords and len(item) > NCHAR:
                        lab3[item] = counter

            if lab3.keys():
                print('***** Sample entries: *****')   
                for k in random.choices(list(lab3.keys()), k=CHOICES):
                    print(k, lab3[k])

                print('***** Top Keys: *****')
                tk = lab3.topKeys(100)
                for tt in tk:
                    print(tt, len(lab3[tt]))

            lab3.clear()
            print(lab3)

    t.toc() #elapsed time
    print('*' * 13)