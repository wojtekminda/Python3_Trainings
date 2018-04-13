# --- Pierwszy sposob --- #
osoba = dict()
print(osoba)
print(len(osoba))

osoba['name'] = 'Jan'
osoba['surname'] = 'Kowalski'
osoba['age'] = 32

print(osoba)
print(len(osoba))

print(osoba['name'])
print(len(osoba['name']))

# --- Drugi sposob --- #
osoba2 = {}
print(osoba2)

osoba2['name'] = 'Adam'
osoba2['surname'] = 'Nowak'
osoba2['age'] = 40

print(osoba2)
print(len(osoba2))

# --- Petla for --- #
for key in osoba:
    print(key, osoba[key])
