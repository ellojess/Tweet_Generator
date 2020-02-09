from flask import Flask
# from word_frequency import histogram
from python_quote import random_python_quote
import random


app = Flask(__name__)

@app.route('/')
def generate_words():
    # lines = get_lines("./words.txt")
    # myhistogram = histogram(lines)
    sentence = ""

    num_words = 10 
    for i in range(num_words):
        # word = weighted_sample(myhistogram)
        word = random_python_quote()
        sentence += " " + word

    return sentence


if __name__ == '__main__':
    app.run()

# from flask import Flask
# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return "Hello World!"

# if __name__ == '__main__':
#     app.run()