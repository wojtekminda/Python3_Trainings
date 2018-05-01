'''
Write a script which repeatedly asks the user to provide a word until he or she provides an empty word (hits ENTER immediately).
Then, print all of the provided words in the same order except for the shortest and longest ones.
In the following example 'he' and 'up' are not printed, because they are the shortest words.
Similarly 'barking' is not printed, because it is the longest word.
'''

word = input("Wprowadz slowo (albo nacisnij ENTER, aby zakonczyc): ")
shortest = len(word)
longest = len(word)
words = list()

while word:
    words.append(word)

    if len(word) < shortest:
        shortest = len(word)
    if len(word) > longest:
        longest = len(word)

    word = input("Wprowadz slowo (albo nacisnij ENTER, aby zakonczyc): ")

print("\nShortest word ->", shortest, "signs")
print("Longest word ->", longest, "signs")
print("List of words ->", words)

print("\nBelow words list without shortest and longest words:")
for word in words:
    #if len(word) > shortest and len(word) < longest:
    if shortest < len(word) < longest:
        print(word)
