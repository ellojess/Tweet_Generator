import random
import sys as sys 
from python_quote import random_python_quote

'''
- test with " python3 rearrange.py how now brown cow "

- takes words as list in command line
- split list 
- shuffle words to a random order 
- join list 
'''

sentence = sys.argv[1:]
# print(sentence)

def rearrange(sentence):
    for word in sentence:
        words = word.split(' ')
        random.shuffle(words)
    return ' '.join(words)
    # print(words)

print(rearrange(sentence))

# get the command line arguments with sys 
# if __name__ == "__main__":
#     # args = sys.argv
#     # words = args[1:]
#     print(rearrange(sentence))
#     # print(words)