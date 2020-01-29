import random

'''
List of example quotes 
'''
quotes = ("It's just a flesh wound.",
          "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

'''
Function returns a random quote from list 
'''
def random_python_quote():
    rand_index = random.randint(0, len(quotes) - 1)
    return quotes[rand_index]

'''
Entry point of program, runs random_python_question() and returns quote
'''
if __name__ == '__main__':
    quote = random_python_quote()
    print(quote)