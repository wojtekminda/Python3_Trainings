### get() - First argument
person = {'first_name': 'John', 'last_name': 'Smith'}

name = person.get('first_name')
age = person.get('age')

if not name:
   name = 'User'

if not age:
    age = '???'

print(name + ', you are', age, 'yo.')
print(person)


### get() - Second argument
person = {'first_name': 'John', 'last_name': 'Smith'}

name = person.get('first_name', 'User')
age = person.get('age', '???')

print(name + ', you are', age, 'yo.')
print(person)


### setdefault()
person = {'first_name': 'John', 'last_name': 'Smith'}

name = person.setdefault('first_name', 'User')
age = person.setdefault('age', '???')

print(name + ', you are', age, 'yo.')
print(person)
