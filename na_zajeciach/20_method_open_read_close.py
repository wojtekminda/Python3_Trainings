directory = '.\\encodings\\'
file = 'blad_utf-8'

print(directory + file)

f = open(directory + file, encoding="utf-8")
data = f.read()
f.close()

print(data)
