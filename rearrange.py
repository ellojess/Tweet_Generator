import random
import sys as sys 

'''
TODO: 
- fix split words.txt list 
- test with " python3 rearrange.py how now brown cow "
'''

sentence = sys.argv[1:]

def rearrange(sentence):
    words = sentence.split()
    for word in words:
        random.shuffle(words)
        print(words)
    return ' '.join(words)
    print(words)

# get the command line arguments with sys 
if __name__ == "__main__":
    print(rearrange(sentence))
    args = sys.argv
    words = args[1:]
    print(words)