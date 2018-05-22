words = []

word = input('Provide a word: ')

while word:
    words.append(word)
    word = input('Provide a word: ')

order = input('Please, choose sorting order (normal/reverse): ')

if order == 'normal':
    sorted_words = sorted(words)
elif order == 'reverse':
    sorted_words = sorted(words, reverse=True)

for word in sorted_words:
    print(word)
