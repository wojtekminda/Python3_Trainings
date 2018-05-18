'''
Write make_dict() function, which accepts a single argument.
The argument is a sequence (a string, a tuple or a list).
The function creates and returns a dictionary based on the sequence.
It obtains key-value pairs from the sequence by taking consecutive pairs of elements from the sequence.
It raises ValueError when the length of the sequence is odd. Compare example usage:

# prints: {'a': 1}
print(make_dict(
    ['a', 1]  # length 2
))

# prints: {'b': 2, 'a': 1, 'c': 3, 'd': 4}
print(make_dict(
    ['a', 1, 'b', 2, 'c', 3, 'd', 4]  # length 8
))

# raises ValueError
make_dict(
    ['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e']  # length 9
)
'''

def make_dict(sequence):
    sequence_dict = {}
    if len(sequence) % 2 != 0:
        raise ValueError('sequence must have even length')
    else:
        for i, item in enumerate(sequence):
            if i % 2 == 0:
                key = item
            else:
                value = item
                sequence_dict[key] = value
    return sequence_dict

# prints: {'a': 1}
print(make_dict(['a', 1]))

# prints: {'b': 2, 'a': 1, 'c': 3, 'd': 4}
print(make_dict(['a', 1, 'b', 2, 'c', 3, 'd', 4]))

# prints: {'e': 5, 'f': 6, 'g': 7, 'h': 8}
print(make_dict(('e', 5, 'f', 6, 'g', 7, 'h', 8)))

# prints: {'t': 'e', 's': 't', 'o': 'w', 'a': 'n', 'i': 'e'}
print(make_dict('testowanie'))

# raises ValueError
make_dict(['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e'])
