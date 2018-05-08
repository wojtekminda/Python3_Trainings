'''
Write put_many() function which takes two arguments: a list and a dictionary.
It treats every element of the list as a potential key in the dictionary.
The function modifies the given list by substituting every element with a matching value in the dictionary.
If there is no matching value (i.e. the key is missing), the element is left unchanged:
keys = ['a', 'b', 'c', 'd', 'a']
mapping = {'a': 13, 'c': 9, 'e': 7}
print(keys)  # prints: ['a', 'b', 'c', 'd', 'a']
put_many(keys, mapping)
print(keys)  # prints: [13, 'b', 9, 'd', 13]

Then, write get_many() function which behaves identically, but, instead of modifying the given list argument,
it returns a new list which reflects the changes. Try to write get_many() so that its implementation calls put_many():
keys = ['a', 'b', 'c', 'd', 'a']
mapping = {'a': 13, 'c': 9, 'e': 7}
print(keys)    # prints: ['a', 'b', 'c', 'd', 'a']
result = get_many(keys, mapping)
print(keys)    # prints: ['a', 'b', 'c', 'd', 'a']
print(result)  # prints: [13, 'b', 9, 'd', 13]
'''

def put_many(keys, mapping):
    for i, key in enumerate(keys):
        if key in mapping:
            keys[i] = mapping[key]

def get_many(keys, mapping):
    keys_copy = list(keys)
    put_many(keys_copy, mapping)
    return keys_copy

keys = ['a', 'b', 'c', 'd', 'a']
mapping = {'a': 13, 'c': 9, 'e': 7}

print(keys)     # prints: ['a', 'b', 'c', 'd', 'a']
put_many(keys, mapping)
print(keys)      # prints: [13, 'b', 9, 'd', 13]

keys = ['a', 'b', 'c', 'd', 'a']
mapping = {'a': 13, 'c': 9, 'e': 7}

print(keys)     # prints: ['a', 'b', 'c', 'd', 'a']
result = get_many(keys, mapping)
print(keys)     # prints: ['a', 'b', 'c', 'd', 'a']
print(result)   # prints: [13, 'b', 9, 'd', 13]
