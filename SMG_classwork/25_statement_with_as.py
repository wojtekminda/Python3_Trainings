directory = '.\\files\\'
file = 'ankieta.txt'
encoding_name = 'utf-8'

print("Sciezka do pliku:\n" + directory + file)

with open(directory + file, encoding=encoding_name) as f:
    for line in f:
        print(line, end="")
