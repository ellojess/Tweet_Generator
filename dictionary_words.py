import random
import sys as sys 

'''
Select a random set of words from words file and store in a data type
Put the number of words requested together into a "sentence"
Output sentence
'''
def random_sentence(sentence_len, words):
    sentence = ""
    for _ in range(sentence_len):
        word = random.choice(words)
        sentence += word + " "
    return sentence

# f.close()

if __name__ == "__main__":
    with open('words.txt', 'r') as f:
        words = f.read().split('\n')
    # print(words)
    # words = ['orange', 'blue', 'yellow', 'red', 'green', 'pink']
    sentence_len = int(sys.argv[1])
    print(sentence_len)
    print(random_sentence(sentence_len, words))