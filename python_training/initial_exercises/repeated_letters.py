
from string import ascii_lowercase
from math import floor

from python_training.utilities.string_utilities import english_word_list

word_list = english_word_list()


# get all the letters not appearing double in any word
for letter in ascii_lowercase: # all letters
    exists = False
    for word in word_list:
        if (letter * 2) in word:
            exists = True
            break

    if not exists:
        print("There are not english words containing twice the letter : {}".format(letter))


# getting all the words containing uu
for word in word_list:
        if 'uu' in word:
            print(word)

# getting all the words containing all vowels
for word in word_list:
    contains = True
    for v in list('aeiou'):
        if v not in word:
            contains = False
            break
    
    if contains:
        print('The word {} contains all the vowels'.format(word))

# find longest palindrome
def is_palindrome(word):
    l = len(word)
    if(l > 2):
        m = floor(l /2)
        l -= 1
        i = 0
        while(i<m):
            if(word[i] == word[-(i + 1)]):
                i += 1
            else:
                break
        return i == m
    else:
        return False

w_l = word_list
i = 0
l = len(w_l)
longest = ''
longest_length = 0    
while i < l:
    word = w_l[i]
    if(is_palindrome(word)):
        if(len(word)) > longest_length:
            longest = word
            longest_length = len(word)
            

        i += 1

print(longest)
