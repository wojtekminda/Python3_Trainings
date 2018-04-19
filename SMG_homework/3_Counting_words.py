'''
Write a script which repeatedly asks the user to provide a word until he or she provides an empty word (hits ENTER immediately).
Then, print the list of provided words. Each printed word should be accompanied by the number of times it was provided.
'''

words_list = list()

word = input("Provide a word (or hit ENTER to print results): ")

while word:
    words_list.append(word)
    word = input("Provide a word (or hit ENTER to print results): ")

for word_L1 in words_list:
    counter = 0
    for word_L2 in words_list:
        if word_L1 == word_L2:
            counter = counter + 1
    print(word_L1, "->", counter)
