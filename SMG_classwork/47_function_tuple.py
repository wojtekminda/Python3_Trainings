### Pierwsza metoda -> tuple()
t1 = tuple()

t1 = ('Anna', 'Warsaw', 23)
print(t1)
print(len(t1))

d = {(3, 4): 5}
print(d)

### Druga metoda -> ()
t2 = ('Anna',)
print(t2)

# !!!Tuples are immutable!!! - AttributeError
t1.append('aaa')
