from python_training.utilities.string_utilities import english_word_list
from python_training.utilities.string_utilities import shakespeare_sonnets


import timeit

# get the total of novel words
# (words in the sonnets but not contained in the word list)
shakespeare = shakespeare_sonnets()
all_text = ' '.join(shakespeare)
word_list = english_word_list()
all_words = ''.join(word_list)

counter = 0
novel_words = []
start_time = timeit.default_timer()
for word in shakespeare:
    if(word not in all_words):
        counter += 1
        novel_words.append(word)

print(counter, novel_words)
print(timeit.default_timer() - start_time)

counter = 0
novel_words = []
start_time = timeit.default_timer()
for word in shakespeare:
    if(word not in word_list):
        counter += 1
        novel_words.append(word)

print(counter, novel_words)
print(timeit.default_timer() - start_time)
