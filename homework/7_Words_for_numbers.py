'''
Write a script which asks the user to enter some numbers separated by spaces.
It then prints the smallest and the largest of entered numbers, as well as sum of them.
To make things more interesting, however, the numbers provided by the user are expressed using English words.
That is user may input: one, two, three, four, five, six, seven, eight, nine, ten (you may also allow other additional words such as zero, thirteen, dozen, 1/4, thousand, pi, XIX).
Example session with the script:
Enter some numbers: nine three four two three
Min: 2
Max: 9
Sum: 21
'''

numbers_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10
}

numbers = input('Enter some numbers [English words]: ')
numbers = numbers.split()
print(numbers)

minimum = numbers_dict[numbers[0]]
maximum = numbers_dict[numbers[0]]
sum_of_numbers = 0
for elem in numbers:
    number = numbers_dict[elem]
    if number < minimum:
        minimum = number
    if number > maximum:
        maximum = number
    sum_of_numbers = sum_of_numbers + number

print('Minimum:', minimum)
print('Maximum:', maximum)
print('Sum:', sum_of_numbers)
