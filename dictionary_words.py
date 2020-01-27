import random
import sys as sys 

'''
Weird bug found when testing in terminal, ex: 
$ python3 dictionary_words.py 5
[first run] only prints out 3 words 
[second run] prints out 5
[third run and every run after that] prints out 4 words
'''

words = open('words.txt', 'r')
words = words.read().split('\n')
sentence_len = int(sys.argv[1])
# print(sentence_len)

'''
Select a random set of words from words file and store in a data type
Put the number of words requested together into a "sentence"
Output sentence
'''
def random_sentence(sentence_len):
    sentence = []
    for word in range(sentence_len):
        word = random.choice(words)
        sentence.append(word)
    return ' '.join(sentence)

# f.close()

if __name__ == "__main__":
    print(random_sentence(sentence_len))