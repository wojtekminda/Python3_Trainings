numbers = input("Podaj liczby jedna po drugiej, bez przecinkow i nacisnij ENTER: ")

if numbers == "":
    print("Nic nie podales...")

else:
    numbers_list = numbers.split()

    numbers_list_float = list()
    for number in numbers_list:
        number = float(number)
        numbers_list_float.append(number)

    length = len(numbers_list)
    sum_of_numbers = sum(numbers_list_float)
    minimum = min(numbers_list_float)
    maximum = max(numbers_list_float)
    average = sum_of_numbers / length

    print(numbers)
    print(numbers_list)
    print(numbers_list_float)
    print("Length of list:", length)
    print("Sum of numbers:", sum_of_numbers)
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", average)
