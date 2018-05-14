'''
Write replace_words() function which takes two arguments:
• A text (str) in which some of the words are going to be replaced.
• A mapping (dict) from words to be replaced (str) to the new replacement words (str).
The function returns text with all words which appear in the mapping replaced.
A word is defined as having a single space or the beginning of the string on its left and a single space
or the end of the string on its right.

Example usage of the function:
TEXT = "We went to Wellington to find a nice place to eat. We think Wellington is nice!"

modified = replace_words(TEXT, {"Wellington": "Warsaw", "nice": "cool"})
print(modified)
# prints: We went to Warsaw to find a cool place to eat. We think Warsaw is nice!

print(replace_words(modified, {"We": "You"}))
# prints: You went to Warsaw to find a cool place to eat. You think Warsaw is nice!

Note that in the above example TEXT contains words "nice" and "nice!", so only the first one is replaced.
Just split on a single space!
'''

def replace_words(to_replace, replacement_dict):
    # PC: To rozwiazanie jest zupelnie dobre
    #     (za wyjatkiem mojej drugiej uwagi nizej).
    #     Natomiast Twoja funkcja tworzy dwie listy,
    #     a moglaby tworzyc tylko jedna.
    new_text = []
    for word in to_replace.split():
        # PC: Ponizsza petla jest niepotrzebna.
        #     Nie po to istnieja slowniki.
        #     Zastanow sie, czym ja zastapic.
        for key in replacement_dict:
            if word == key:
                word = replacement_dict[key]
        new_text.append(word)
    return ' '.join(new_text)

text = "We went to Wellington to find a nice place to eat. We think Wellington is nice!"
print(text)

replacement_dictionary = {"Wellington": "Warsaw", "nice": "cool"}
print(replacement_dictionary)

modified = replace_words(text, replacement_dictionary)
print(modified)
