people = []

cont = 'yes'

while cont == 'yes':
    person = {}
    person['Name'] = input('Name: ')
    person['Surname'] = input('Surname: ')
    person['Age'] = input('Age: ')
    people.append(person)
    cont = input('Do you want to add next person? [yes/no] ')

print(people)
