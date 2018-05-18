'''
Write input_int() function which asks the user to provide an integer number
and returns it (as a number, not as a string). It accepts up to 3 arguments:
1. An optional prompt (like input() built-in function).
2. An optional minimum acceptable number (there is no minimum by default).
3. An optional maximum acceptable number (there is no maximum by default).
The function keeps asking the user until she provides a well-formed integer number within range.

Example usage of the function:
a = input_int("Enter an integer: ")
b = input_int("Enter a positive integer: ", 1)
c = input_int("Enter an integer not greater than 8: ", largest=8)
d = input_int("Enter an integer (4..8): ", 4, 8)
print("Provide another integer (4..8):")
e = input_int(smallest=4, largest=8)
print("Your numbers multiplied by 2:", a * 2, b * 2, c * 2, d * 2, e * 2)

Example session with the script:
Enter an integer: cake
Enter an integer: 3.4
Enter an integer: -5
Enter a positive integer: -10
Enter a positive integer: 0
Enter a positive integer: 1000
Enter an integer not greater than 8: 1000
Enter an integer not greater than 8: 7
Enter an integer (4..8): 1
Enter an integer (4..8): 4
Provide another integer (4..8):
9
8
Your numbers multiplied by 2: -10 2000 14 8 16
'''

def input_int(prompt='', smallest=None, largest=None):
    number = input(prompt)
    while number:
        try:
            number = int(number)
            if smallest == None and largest == None:
                return number
            elif largest == None:
                if not number < smallest:
                    return number
            elif smallest == None:
                if not number > largest:
                    return number
            else:
                if not (number < smallest or number > largest):
                    return number
        except ValueError as exc:
            print(exc)
        number = input(prompt)

a = input_int("Enter an integer: ")
print(a)

b = input_int("Enter a positive integer: ", 1)
print(b)

c = input_int("Enter an integer not greater than 8: ", largest=8)
print(c)

d = input_int("Enter an integer (4..8): ", 4, 8)
print(d)

print("Provide another integer (4..8):")
e = input_int(smallest=4, largest=8)

print("Your numbers multiplied by 2:", a * 2, b * 2, c * 2, d * 2, e * 2)
