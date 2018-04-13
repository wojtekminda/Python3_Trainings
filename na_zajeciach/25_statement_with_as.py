directory = '.\\files\\'
file = 'ankieta.txt'
encoding_name = 'utf-8'

print("Pelna sciezka to:\n" + directory + file)

with open(directory + file, encoding=encoding_name) as f:
    for line in f:
        print(line, end="")
