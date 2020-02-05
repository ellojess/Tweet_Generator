from flask import Flask
from word_frequency import histogram
from sample import 

app = Flask(__name__)

@app.route('/')
def generate_words():
    lines = get_lines("./words.txt")
    myhistogram = histogram(lines)
    sentence = ""

    num_words = 10 
    for i in range(num_words):
        word = weighted_sample(myhistogram)
        sentence += " " + word

    return sentence


if __name__ == '__main__':
    app.run()