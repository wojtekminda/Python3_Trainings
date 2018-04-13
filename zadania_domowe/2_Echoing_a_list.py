'''
Write a script which repeatedly asks the user to provide a word until he or she provides an empty word (hits ENTER immediately).
Then, print each of the provided words in a separate line (in the same order).
'''

words_list = list()

word = input("Provide a word (or hit ENTER to print results): ")

while word:
    words_list.append(word)
    word = input("Provide a word (or hit ENTER to print results): ")

i = 0
while i < len(words_list):
    print(words_list[i])
    i = i + 1
