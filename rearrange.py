import random
from random import shuffle
import sys as sys 

# get the command line arguments with sys 
if __name__ == "__main__":
    '''
    main function takes words in 
    command line as argument and shuffles words
    - test with " python3 rearrange.py how now brown cow "

    - takes words as list in command line
    - shuffle words to a random order 
    - join list 
    '''
    words = sys.argv[1:]
    shuffle(words)
    print(" ".join(words))