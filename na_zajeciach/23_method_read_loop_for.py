directory = '.\\encodings\\'
file = 'multiline_ascii'
encoding_name = 'utf-8'

print("Pelna sciezka to:\n" + directory + file)

f = open(directory + file, encoding = encoding_name)

x = 0
for line in f:
    print("Linia nr", x, "->", line, end="")
    x = x + 1

f.close()
