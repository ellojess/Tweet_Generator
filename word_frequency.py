import random 

def histogram(words):
    '''
    dictionary histogram
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

def list_histogram(words):
    '''
    Loop through each pair of words from get_pairs and
    append the pair to histogram for a list of lists 
    '''
    list_words = get_pairs(words)
    histogram = []
    i = 0
    while i < len(list_words) - 1:
        list = []
        list.append(list_words[i])
        list.append(list_words[i+1])
        histogram.append(list)
        # exit while loop
        i += 2
    return histogram

# helper function for list_histogram
def get_pairs(words):
    '''
    Loop through and track each unique word, and the number of time it appears 
    increase count every time word appears in list 
    append word and word count to a list 
    '''
    pairs = []
    i = 0
    while len(words) > 0 and i < len(words):
        word = words[i]
        count = 1
        index = i + 1
        while index < len(words):
            if words[index] == word:
                count += 1
                words.pop(index)
                index = index - 1
            index += 1
        pairs.append(word.rstrip())
        pairs.append(count)
        # exit while loop
        i += 1
    return pairs

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
    l = list_histogram(words)
    u = unique_words(h)
    f = frequency(h, 'yam')
    print(h)
    print(l)
    print(u, f)