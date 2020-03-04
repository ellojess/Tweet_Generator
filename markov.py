from dictogram import Dictogram

class MarkovChain:

    def __init__(self, word_list):

        #The Markov chain will be a dictionary of dictionaries
        #Example: for "one fish two fish red fish blue fish"
        #{"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
         self.markov_chain = self.build_markov(word_list)
         self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys():
                #get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                #add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else:
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        # generate sentence num_words long using the markov chain
        first_word = random.choice(list(self.markov_chain.keys()))
        print("FIRST WORD IS", first_word)
        sentence = first_word + " "
        index = 0
        current_word = first_word
        while (index < num_words):
            current_word_dictogram = self.markov_chain[current_word]
            print("From word =", current_word, "DICTOGRAM I AM SAMPLING IS", current_word_dictogram)
            random_weighted_word =  current_word_dictogram.sample()
            print("Sample returned is", random_weighted_word)
            current_word = random_weighted_word 
            if index == num_words - 1:
                sentence += current_word + "."
                break
            else: #if not last word, add a space in the end
                sentence += current_word + " "
            index += 1
        print(sentence)

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))