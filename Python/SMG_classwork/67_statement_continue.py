names = ('Alice', 'Bob', 'Charlie', 'Debbie', 'Emma', 'Fred')

for name in names:
    print('<', end='')
    if name == 'Charlie':
        continue
    print(name, end='')
    print('>', end='')
print('STOP')
