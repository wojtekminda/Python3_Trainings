'''
Write a script which asks the user to provide a list of words separated by commas (in a single line).
The script then analyzes the provided text and prints the list of words.
'''

print("Please, provide a comma-separated list of words:")
words_input = input()
words_list = list()

word = ''
i = 0
while i < len(words_input):
    if words_input[i] == ',':
        words_list.append(word)
        word = ''

    elif words_input[i] == ' ':
        pass

    else:
        word = word + words_input[i]

    if i == len(words_input) - 1:
        words_list.append(word)

    i = i + 1

print(words_list)
