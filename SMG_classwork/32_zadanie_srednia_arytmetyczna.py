number = input("Podaj jakas liczbe (aby zakonczyc -> nacisnij ENTER): ")

sum_of_numbers = 0
counter = 0
while number:
    number = float(number)
    sum_of_numbers = sum_of_numbers + number
    number = input("Podaj jakas liczbe (aby zakonczyc -> nacisnij ENTER): ")
    counter = counter + 1

average = sum_of_numbers/counter

print("Srednia:", average)
