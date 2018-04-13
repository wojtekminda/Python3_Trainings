directory = '.\\encodings\\'
file = 'multiline_ascii'
encoding_name = 'utf-8'

print("Pelna sciezka to:\n" + directory + file)

f = open(directory + file, encoding=encoding_name)

data = f.read(11)
print(data, end="")
data = f.read(5)
print(data, end="")

f.close()
