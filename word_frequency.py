import random 

'''
function which takes a source_text argument
(can be either a filename or the contents of 
the file as a string, your choice) 
and return a histogram data structure that 
stores each unique word along with the 
number of times the word appears in the source text
'''

def histogram(words):

    # Iterate over each word in line
    for word in words: 
        # Check if the word is already in dictionary 
        if word in word_histogram.keys(): 
            # Increment count of word by 1 
            word_histogram[word] +=  1
        else: 
            # Add the word to dictionary with count 1 
            word_histogram[word] = 1

    # Print the contents of dictionary 
    for key in word_histogram.keys(): 
        print(key, ":", word_histogram[key]) 

'''
function that takes a histogram argument 
and returns the total count of unique words in the histogram
'''
def unique_words(words):
    # count word_histogram keys 
    print(len(word_histogram))

'''
function that takes a word and histogram 
argument and returns the number of times that word appears in a text
'''
def frequency():
    pass

if __name__ == "__main__":
    filename = 'words.txt'
    # filehandle = open(filename, 'r') 
    # lines = filehandle.readlines()
    # histogram(filehandle)
    # filehandle.close()
    word_histogram = {}

    with open(filename, 'r') as f:
        words = f.read().split(' ')
        histogram(words)
        unique_words(words)
    # print(words)    