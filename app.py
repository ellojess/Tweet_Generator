from flask import Flask, request, url_for
from listogram import Listogram
from dictogram import Dictogram
from dictionary_words import random_sentence
# from markov import MarkovChain
import os
import sys

'''
TODO: Still need to figure out how to get listogram, dictogram, and 
markov chain properly working in Flask app 
'''

app = Flask(__name__)

@app.route('/')

def generate_words(): 
    with open('words.txt', 'r') as f:
        words = f.read().split(' ')

    listo = Listogram(words).listogram_samples(10)
    dicto = Dictogram(words).dictogram_samples(10)

    histograms = {
        0: listo,
        1: dicto
    }

    # sentences = [sentence for (index, sentence) in histograms.items()]
    # return sentences
    return random_sentence(5, words)

if __name__ == '__main__':
    app.run()