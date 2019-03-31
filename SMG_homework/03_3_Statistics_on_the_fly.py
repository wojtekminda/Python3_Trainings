'''
Write a script which repeatedly asks the user to provide an integer number until he or she provides an empty string (hits ENTER immediately).
Then, print the smallest, the largest and the sum of entered numbers. Don't use lists in your implementation.
'''

print("Podawaj liczby, a ja znajde najmniejsza, najwieksza oraz podam sume wszystkich wprowadzonych liczb")
print("(Jezeli skonczyles -> nacisnij Enter)\n")
number = input("Podaj liczbe: ")
number = int(number)
minimum = number
maximum = number
suma = 0

while number:

    number = int(number)

    if number < minimum:
        minimum = number

    if number > maximum:
        maximum = number

    suma = suma + number

    number = input("Podaj liczbe: ")

print("Minimum ->", minimum)
print("Maximum ->", maximum)
print("Suma ->", suma)
