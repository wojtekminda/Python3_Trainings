list_of_pairs = []

pair = input('<user> <number> ')

while pair:
    pair = pair.split()
    pair[1] = float(pair[1])
    list_of_pairs.append(pair)
    pair = input('<user> <number> ')

print(list_of_pairs)

for pair1 in list_of_pairs:
    user1 = pair1[0]
    for pair2 in list_of_pairs:
        user2 = pair2[0]
        delta = abs(pair1[1]-pair2[1])
        if delta < 0.1:
            print(user1 + ' --- ' + user2)
