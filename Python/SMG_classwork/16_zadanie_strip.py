words = list()

print("Tworzymy liste slow")
print("(Jezeli wypisales juz wszystkie -> nacisnij Enter)\n")
print("Podaj slowo")
word = input()
word_strip = word.strip()

while word:
    words.append(word_strip)
    print("Podaj slowo")
    word = input()
    word_strip = word.strip()

print(words)
