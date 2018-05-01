directory = '.\\encodings\\'

file = input("Podaj nazwe pliku: ")
encoding_name = input("Podaj typ kodowania: ")

print("Sciezka do pliku:\n" + directory + file)

f = open(directory + file, encoding=encoding_name)
data = f.read()
f.close()

print(data)
