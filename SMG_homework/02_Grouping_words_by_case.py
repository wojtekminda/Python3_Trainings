'''
Write a script which repeatedly asks the user to provide a word until he or she provides an empty word (hits ENTER immediately).
Then, print the list of provided words.
The list should first contain lower-case words, then mixed-case words and finally upper-case words.
Within each group the words are in the same order as they were provided by the user.
'''

#Deklaracja zmiennych
things = list()

#Komunikacja z uzytkownikiem
print("Tworzymy liste twoich rzeczy\n")

#Petla do wprowadzania listy rzeczy
thing = input("Podaj rzecz (albo nacisnij ENTER w celu wydrukowania wynikow): ")
while thing != "":
	things.append(thing)
	thing = input("Podaj rzecz (albo nacisnij ENTER w celu wydrukowania wynikow): ")

#Drukowanie listy rzeczy
#kolejnosc: male, mieszane, duze
i = 0
while i < len(things):
    if things[i] == things[i].lower():
        print(things[i])
    i = i + 1

i = 0
while i < len(things):
    if things[i] != things[i].lower() and things[i] != things[i].upper():
        print(things[i])
    i = i + 1

i = 0
while i < len(things):
    if things[i] == things[i].upper():
        print(things[i])
    i = i + 1
