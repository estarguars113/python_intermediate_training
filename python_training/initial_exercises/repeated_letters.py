
from string import ascii_lowercase

from python_training.utilities.string_utilities import english_word_list

word_list = english_word_list()
for letter in ascii_lowercase: # all letters
    exists = False
    for word in word_list:
        if (letter * 2) in word:
            exists = True
            break

    if not exists:
        print("There are not english words containing twice the letter : {}".format(letter))