import random
import sys as sys 
from python_quote import random_python_quote

'''
TODO: 
- fix split words.txt list 
- test with " python3 rearrange.py how now brown cow "
- 
'''

sentence = random_python_quote()

def rearrange(sentence):
    words = sentence.split()
    random.shuffle(words)
    new_sentence = ' '.join(words)
    print(new_sentence)

# rearrange(sentence)

# get the command line arguments with sys 
if __name__ == "__main__":
    print(rearrange(sentence))
    # args = sys.argv
    # words = args[1:]
    # print(words)