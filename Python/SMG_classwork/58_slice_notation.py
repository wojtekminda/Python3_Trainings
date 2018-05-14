names = ['Alice', 'Bob', 'Charlie', 'Damian', 'Ella', 'Frank', 'Gabriel']

print(names[2:5])
print(names[2:500000])
print(names[-20000:5])
print(names[5:2])
print(names[-5:-2])
print(names[2:])
print(names[:5])
print(names[::2])

print(names[1:3])
names[1:3] = ['Betty', 'Celina']
print(names)
