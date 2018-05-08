names = ('Alice', 'Bob', 'Charlie')
cities = ['Warsaw', 'Cracow', 'Poznan', 'Gdansk']
numbers = [13, 31]

z = zip(names, cities, numbers)
print(z)
print(list(z))

for pair in zip(names, cities):
    print(pair)

for n, c in zip(names, cities):
    print(n, c)
