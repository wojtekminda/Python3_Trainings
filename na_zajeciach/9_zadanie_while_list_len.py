names = list()

print("Tworzymy liste twoich kotow")
print("(Jezeli wypisales juz wszystkie -> nacisnij Enter)\n")
print("Podaj imie kota")
name = input()

while name != "":
    names.append(name)
    print("Podaj imie kota")
    name = input()

#Wypisywanie od przodu listy
print("Wypisywanie od przodu listy")
i = 0
while i < len(names):
    print(names[i])
    i = i + 1

#Wypisywanie od tylu listy
print("\nWypisywanie od tylu listy")
i = 1
while i < len(names)+1:
    print(names[-i])
    i = i + 1
