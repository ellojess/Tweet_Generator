import random 

def histogram(words):
    '''
    takes a word from a source_text
    and return a histogram data structure that 
    stores each unique word along with the 
    number of times the word appears in the source text
    '''
    # Iterate over each word in line
    histogram = {}
    for word in words: 
        histogram[word] = histogram.get(word, 0) + 1
    return histogram

def unique_words(histogram):
    '''
    takes a histogram argument and returns 
    the total count of unique words in the histogram
    '''
    # count word_histogram keys 
    return len(histogram)


def frequency(histogram, word):
    '''
    takes a word and histogram argument and 
    returns the number of times that word appears in a text
    '''
    return histogram.get(word, False)

if __name__ == "__main__":
    '''
    Entry point of program, opens and closes words.txt file for program to use
    Holds empty dictionary for program to use
    '''
    filename = 'words.txt'

    word_histogram = {}

    with open(filename, 'r') as f:
        words = f.read().split(' ')
    h = histogram(words)
    u = unique_words(h)
    f = frequency(h, 'yam')
    print(h, u, f)