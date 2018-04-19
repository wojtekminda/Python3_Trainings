names = list()
cats_counter = 0

print("Tworzymy liste twoich kotow")
print("(Jezeli wypisales juz wszystkie -> nacisnij Enter)\n")
print("Podaj imie kota")
name = input()

while name != "":
    names.append(name)
    print("Podaj imie kota")
    name = input()
    cats_counter = cats_counter + 1

if names == []:
    print("Wyglada na to, ze nie masz zadnego kota...")

if names != []:
    print("Oto lista Toich kotow:")
    print(names)
    print("\nLiczba Twoich kotow to:", cats_counter)
