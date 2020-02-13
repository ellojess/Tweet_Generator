import random
import sys as sys 
from python_quote import random_python_quote

def random_sentence(sentence_len, words):
    '''
    Select a random set of words from words file and store in a data type
    Put the number of words requested together into a "sentence"
    Output sentence
    '''
    sentence = ""
    for _ in range(sentence_len):
        word = random_python_quote(words)
        sentence += word + " "
    return sentence

if __name__ == "__main__":
    '''
    Entry point of program, opens and closes words.txt file for program to use
    Recognizes command line argument with sys.argv[1]
    '''
    with open('words.txt', 'r') as f:
        words = f.read().split(' ')

    sentence_len = int(sys.argv[1])
    print(sentence_len)
    print(random_sentence(sentence_len, words))