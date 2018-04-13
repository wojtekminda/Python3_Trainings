person = {'first_name': 'John', 'last_name': 'Smith'}

if 'first_name' in person:
    name = person['first_name']
else:
    name = 'User'

if 'age' not in person:
    person['age'] = input('Dear ' + name + ', please, tell me your age: ')
    print(person['first_name'], person['last_name'], 'is', person['age'], 'yo.')
