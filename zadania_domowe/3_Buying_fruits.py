'''
Write a script which sells fruits. Three kinds of fruit are available:
1.apples (1 PLN each)
2.bananas (3 PLN each)
3.pears (7 PLN each)
The script repeatedly asks the user to provide a name of fruit until he or she provides an empty string (hits ENTER immediately).
Whenever the user provides a name the script verifies it. If it is an unavailable fruit, the script says so.
Otherwise, the script asks how many pieces of fruit the user wants to buy.
After all this, the script prints the total amount of money required to buy the ordered items.
'''

print("Hi, I sell fruits:")
print("one apple costs 1 PLN ")
print("one banana costs 3 PLN")
print("one pear costs 7 PLN")

to_pay = 0
multiplier = 0

fruit = input("Which fruit would you like to buy (hit ENTER to pay)? ")

while fruit:
    if fruit == "apple":
        multiplier = input("How many of them? ")
        multiplier = int(multiplier)
        to_pay = to_pay + 1*multiplier
    elif fruit == "banana":
        multiplier = input("How many of them? ")
        multiplier = int(multiplier)
        to_pay = to_pay + 3*multiplier

    elif fruit == "pear":
        multiplier = input("How many of them? ")
        multiplier = int(multiplier)
        to_pay = to_pay + 7*multiplier
    else:
        print("I don't have this...")

    fruit = input("Which fruit would you like to buy (hit ENTER to pay)? ")

print("Do zaplaty: ", to_pay)
