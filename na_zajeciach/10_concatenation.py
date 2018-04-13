### Przyklad 1
x = "7"
y = "13"
z = x + y
print(x)		# prints: 7
print(y)		# prints: 13
print(z)		# prints: 713

x = "Hello"
print(x + "!")  # prints: Hello!



### Przyklad 2
x = 3
y = "12"
z = x * y
print(z)        # prints: 121212
print(3 * "ha") # prints: hahaha



### Przyklad 3
employees = ["Ann", "Bob"]
volunteers = ["Chad", "Dan"]
schedule = (employees + volunteers) * 2
print(employees)    # prints: ['Ann', 'Bob']
print(volunteers)   # prints: ['Chad', 'Dan']
print(schedule)		# prints: ['Ann', 'Bob', 'Chad', 'Dan', 'Ann', 'Bob', 'Chad', 'Dan']
