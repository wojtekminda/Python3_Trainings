'''
Write normalize() function which accepts a single argument: a dictionary whose values are assumed to be numbers.
It returns a new dictionary with the same keys, but each value is divided by the sum of all values:
d = {'Alice': 5, 'Bob': 7, 'Charlie': 13}
e = normalize(d)
print(d)  # prints: {'Alice': 5, 'Bob': 7, 'Charlie': 13}
print(e)  # prints: {'Alice': 0.2, 'Bob': 0.28, 'Charlie': 0.52}
'''

def normalize(values):
    sum_of_values = 0
    new_values = {}
    for key in values:
        sum_of_values = sum_of_values + values[key]
    for key in values:
        new_values[key] = values[key] / sum_of_values
    return new_values

d = {'Alice': 5, 'Bob': 7, 'Charlie': 13}
e = normalize(d)
print(d)    # prints: {'Alice': 5, 'Bob': 7, 'Charlie': 13}
print(e)    # prints: {'Alice': 0.2, 'Bob': 0.28, 'Charlie': 0.52}
