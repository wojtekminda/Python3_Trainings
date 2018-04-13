directory = '.\\files\\'
file = 'ankieta.txt'
encoding_name = 'utf-8'

print("Pelna sciezka to:\n" + directory + file)

f = open(directory + file, encoding = encoding_name)

x = 0
yes_counter = 0
no_counter = 0
unk_counter = 0
for line in f:
    if line.strip().endswith('yes'):
        yes_counter = yes_counter + 1
    elif line.strip().endswith('no'):
        no_counter = no_counter + 1
    else:
        unk_counter = unk_counter + 1
    x = x + 1

print("Liczba osob, ktore odpowiedzialy 'yes' ->", yes_counter)
print("Liczba osob, ktore odpowiedzialy 'no' ->", no_counter)
print("Liczba osob, ktore sie pomylily ->", unk_counter)

f.close()
