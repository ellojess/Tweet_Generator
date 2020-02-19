import random
from word_frequency import frequency, histogram

def dict_sample(histogram):
    '''
    dictionary type histogram for stochatic sampling 
    Stochastic sampling takes an element from a 
    given collection at random based on it's weight
    Returns a random word 
    '''
    word_count = 0
    # calculate total word count in source text 
    word_count += sum(hist[word] for word in hist.keys())
    word_range = 0
    histogram = {}
    random_int = random.random()

    for key in hist.keys():
        # calculate how often the word/key value appears in source text file 
        histogram[key] = hist[key]/word_count
        # see if word is in that range 
        if random_int > word_range and random_int <= word_range + histogram[key]:
            # return word within range 
            return key
        # change range to decrease liklihood of same word repeating
        word_range += histogram[key]

if __name__ == "__main__":
    '''
    Entry point of program, opens and closes words.txt file for program to use
    Holds empty dictionary for program to use
    '''
    filename = 'words.txt'

    word_histogram = {}

    with open(filename, 'r') as f:
        words = f.read().split(' ')
        hist = histogram(words)

    print(dict_sample(hist))

# '''
# calculate range
# add frequency to determine range 
# see if word is in that range 

# take random number 
# find word at the index generated by random number 
# return random word 
# '''