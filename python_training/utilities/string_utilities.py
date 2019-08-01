import json


def english_word_list() -> list:
    """
        Get a list of the english words
    """
    path_file = './python_training/utilities/assets/sowpods.txt'
    txt_file = open(path_file)
    return [x.rstrip('\n').lower() for x in txt_file]


def shakespeare_sonnets() -> list:
    """
        Get a list containing shakespeare sonnets
    """
    path_file = './python_training/utilities/assets/sonnets.txt'
    return [x.lower() for l in open(path_file).readlines() for x in set(l.strip().split(' '))]
