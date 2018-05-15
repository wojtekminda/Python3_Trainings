def f():
    print('start f')
    g()
    print('stop f')

def g():
    print('start g')
    h(-5)
    print('stop g')

def h(x):
    print('start h')
    #x = 1 / 0
    if x < 0:
        raise ValueError('x must be non-negative')
    print('stop h')

print('start script')
f()
print('stop script')
