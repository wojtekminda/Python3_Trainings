print(tuple("Alice"))
print(list(reversed("Alice")))

d = {'Alice': 5, 'Bob': 7, 'Charlie': 13}
values = list(d.values())
print(values)

names_t = ('Alice', 'Bob', 'Charlie')
names_l = ['Alice', 'Bob', 'Charlie']
print(names_t == names_l)
print(names_t == tuple(names_l))

names_1 = ['Alice', 'Bob', 'Charlie']
names_2 = names_1       # assign the same list
names_3 = list(names_1) # assign a copy of the list
print(names_1)          # prints: ['Alice', 'Bob', 'Charlie']
print(names_2)          # prints: ['Alice', 'Bob', 'Charlie']
print(names_3)          # prints: ['Alice', 'Bob', 'Charlie']
names_2.append('Dorothy')
print(names_1)          # prints: ['Alice', 'Bob', 'Charlie', 'Dorothy']
print(names_2)          # prints: ['Alice', 'Bob', 'Charlie', 'Dorothy']
print(names_3)          # prints: ['Alice', 'Bob', 'Charlie']
