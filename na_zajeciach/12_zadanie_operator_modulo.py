words = list()

print("Tworzymy liste slow")
print("(Jezeli wypisales juz wszystkie -> nacisnij Enter)\n")
print("Podaj slowo")
word = input()

while word != "":
    words.append(word)
    print("Podaj slowo")
    word = input()

print("Powiedz po ile slow w linii chcesz wypisywac")
number_of_words = input()
int_number_of_words = int(number_of_words)

print("Wypisywanie slow -> po", int_number_of_words, "w linijce")
i = 0
while i < len(words):
    print(words[i], end=" ")
    if i % int_number_of_words == int_number_of_words - 1:
        print()
    i = i + 1
