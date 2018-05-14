def manhattan_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

distance = manhattan_dist(5, 4, 9, 7)

print(distance)

print(manhattan_dist(5, 4, 9, 7) * 2)
