file = '.\\files\\ankieta.txt'
encoding_name = 'utf-8'

print("Pelna sciezka to:\n" + file)

word = input("Podaj slowo: ")

with open(file, encoding=encoding_name) as f:
    line_number = 1
    for line in f:
        if word in line:
            print(line_number, line, end="")
        line_number = line_number + 1
