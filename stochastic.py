# import random
# from word_frequency import unique_words, frequency, histogram

# def stoch(word_histogram):
#     ''' Lists  list_hist
#     Stochastic sampling means taking an element from a given collection at random 
#     This returns a list of percentages of word frequencies in a histogram
#     '''

#     percentages = []

#     total_wc = 0    # total word count
#     for item in histogram:
#         total_wc += int(item[1])

#     for item in histogram:
#         percent = (item[1] / total_wc) * 100   # calculate percentage based on freq / total
#         instance = (item[0], percent)
#         percentages.append(instance)

#     return percentages

        


# if __name__ == "__main__":
#     listo_histo = histogram("words.txt")
#     print(stoch(listo_histo))