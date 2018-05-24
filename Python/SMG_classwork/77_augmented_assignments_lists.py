a1 = a2 = [1, 2]
b1 = b2 = [1, 2]
a1 += [3]           # uses __iadd__, modifies a1 in-place
b1 = b1 + [3]       # uses __add__, creates new list, assigns it to b1
print(a2)           # [1, 2, 3] - a1 and a2 are still the same list
print(b2)           # [1, 2] - whereas only b1 was changed
