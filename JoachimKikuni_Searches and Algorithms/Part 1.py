#JoachimKikuni

import wordlist

def linear_word_finder(word):
    
    index = 0
    for entry in wordlist.words:
        if entry == word:
            return index
        else:
            index += 1
print(linear_word_finder("Jacob"))


def binary_word_finder(word)
