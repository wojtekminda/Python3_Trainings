file = '.\\files\\test_write.txt'
encoding_name = 'utf-8'

print("Pelna sciezka to:\n" + file)

# r -> read
# w -> write
# a -> append

with open(file, 'w') as f:
    f.write("dupa")
    f.write('\n')
    f.write("zbita")

print("Utworzono plik ->", file)
