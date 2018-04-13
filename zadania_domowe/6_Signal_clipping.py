'''
Write a script which asks the user to enter floating point signal values separated by spaces.
The script echoes back a list of those values clipped into [-1; 1] range (i.e. values lower than -1 become -1 and values greater than 1 become 1).
Example:
Enter signal values: -0.1 -0.6 -0.9 -1.2 -1.3 -1.1 -0.8 -0.4 0.1 0.5 0.9 1.2
[-0.1, -0.6, -0.9, -1.0, -1.0, -1.0, -0.8, -0.4, 0.1, 0.5, 0.9, 1.0]
'''

values = input('Enter signal values: ')
values = values.split()

clipped_values = []
for value in values:
    value = float(value)
    if value > 1.0:
        value = 1.0
    if value < -1.0:
        value = -1.0
    clipped_values.append(value)

print(values)
print(clipped_values)
