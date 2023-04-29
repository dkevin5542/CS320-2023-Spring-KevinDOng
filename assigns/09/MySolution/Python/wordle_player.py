########################
# HX-2023-04-15: 20 points
########################
"""
Given a history of wordle hints, this function returns a
word as the player's guess.
"""
import nltk
nltk.download('words')
from nltk.corpus import words
########################################################################
def wordle_guess(hints):
    setofwords = [y for y in set(words.words()) if len(y) == len(hints[0]) ]
    def word_is_legal(word):
        return word in setofwords
    next_guess = ""
    not_these = ""
    words_to_look_for = []
    
    tried_these = ["".join([x[1] for x in y]) for y in hints]
    
    #see real combination
    for i in range(len(hints[0])):
        found = False
        for tup in hints:
            if tup[i][0] == 1 and found == False:
                found = True
                next_guess += tup[i][1]
            if tup[i][0] == 0 and not(tup[i][1] in not_these) and not((2,tup[i][1]) in tup) and not((1,tup[i][1]) in tup) :
                not_these += tup[i][1]
            if tup[i][0] == 2 and not(tup[i][1] in words_to_look_for):
                words_to_look_for += [(i,tup[i][1])]
        if (found == False):
            next_guess += "_"
    #print(not_these)
    if not("_" in next_guess):
        return next_guess
    for tup in words_to_look_for:
        not_these = not_these.replace(tup[1], "")
    for word in setofwords:
        nope = False
        for ch in word:
            if (ch in not_these):
                nope = True
                break
        if (nope == True):
            continue
        if (word in tried_these):
            continue
        for i in range(len(hints[0])):
            if (next_guess[i] == "_"):
                "skip"
            elif not(next_guess[i] == word[i]):
                nope = True
                break
        if (nope == False):
            for tup in words_to_look_for:
                if (word.find(tup[1]) == tup[0]) or not(tup[1] in word) :
                    nope = True
                    break
        if (nope == True):
            continue
        else:
            return word
    
    return None
    raise NotImplementedError
########################################################################
