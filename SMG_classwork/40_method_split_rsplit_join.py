### Method: split()
s = '  Hello  ==    bye  == ala ma kota'
print(s.split())
print(s.split('=='))
print(s.split('='))
print(s.split(' '))
print(s.split('==', 1))
print(s.split(None, 2))
print(s.split(maxsplit=2))


### Method: rsplit()
t = 'ala, bob, charlie, debbie, ella'
print(t.rsplit(', ', 2))


### Method: join()
list = ['ala', 'bob', 'charlie', 'debbie']
separator = '-'
print(separator.join(list))
