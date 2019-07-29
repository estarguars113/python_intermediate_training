import json

"""
    Get a list of the english words
"""
def english_word_list() -> list:
    path_file = './python_training/utilities/assets/words_dictionary.json'
    with open(path_file) as json_file:
        words = json.load(json_file)
        return list(words.keys())


