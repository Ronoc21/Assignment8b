# Name: Conor Smith
# Date: 5/19/21
# Description: A function that takes two strings and returns a list of all words that appear in both of the original strings

def words_in_both(string_1, string_2):
    """function that takes two strings converts all words to lower case and returns words that appear in both strings"""
    string_1 = string_1.lower().split()
    string_2 = string_2.lower().split()
    both = []
    for x in string_1:
        if (x in string_2):
            both.append(x)
    return both

#print(words_in_both("cAr car CAR caR Jack was the tallest", 'Jack was tallest of all cars CAR cAr'))