'''
Write check() function which calculates the sum of points of a filled examination form.
The first argument to the function is a list of dictionaries. Each dictionary has 'answer' and 'points' keys.
The value assigned to 'answer' is a string holding the correct answer.
The value assigned to 'points' is the number of points one gets when providing the correct answer
(for incorrect answer the number of points is zero).
The second argument to the function is a list of strings. Each string is an answer (correct or incorrect).
Assume this list and the list form the first argument are of the same length.
The third argument, as_perc, is optional and defaults to False. When False, the function returns a tuple of two numbers:
the number of points for correctly answered question and the number of points that would be granted
if all the answers were correct. When True, only one number is returned:
percentage calculated from the two numbers mentioned previously.
Example usage of the function:

exam_key = [
    {'answer': 'b', 'points': 2},
    {'answer': 'c', 'points': 2},
    {'answer': 'a', 'points': 1},
    {'answer': 'c', 'points': 1},
    {'answer': 'b', 'points': 1},
    {'answer': 'b', 'points': 1},
    {'answer': 'c', 'points': 4}
]

answers1 = ['b', 'c', 'a', 'c', 'b', 'b', 'c']
answers2 = ['b', 'd', 'd', 'c', 'b', 'a', 'c']

# prints: (12, 12) 100.0
print(
    check(exam_key, answers1),
    check(exam_key, answers1, as_perc=True)
)

# prints: (8, 12) 66.66666666666667
print(
    check(exam_key, answers2),
    check(exam_key, answers2, as_perc=True)
)
'''

def check():
    pass
