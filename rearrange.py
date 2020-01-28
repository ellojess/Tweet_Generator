import random
from random import shuffle
import sys as sys 

'''
- test with " python3 rearrange.py how now brown cow "

- takes words as list in command line
- split list 
- shuffle words to a random order 
- join list 
'''

# get the command line arguments with sys 
if __name__ == "__main__":
    words = sys.argv[1:]
    shuffle(words)
    print(" ".join(words))