def f(a, b, c=1, d=2, *args):
    print(a, b, c, d, args)

def g(a, b, c=1, d=2, **kwargs):
    print(a, b, c, d, kwargs)

f(1, 2, 3, 4, 5, 6, 7, 8, 9)
g(1, 2, 3, 4, x=100, y=200)

def h(a, b, c, d, e):
    print(a, b, c, d, e)

z = [5, 6, 7]
h(1, 2, *z)
