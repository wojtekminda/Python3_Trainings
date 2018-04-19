file = '.\\files\\zadanie_28.txt'
encoding_name = 'utf-8'

# r -> read
# w -> write
# a -> append

with open(file, 'w') as f:
    f.write("dupa")
    f.write('\n')
    f.write("zbita")
    f.write('\n')

with open(file, 'a') as f:
    f.write("bardzo")

print("Utworzono plik ->", file)
