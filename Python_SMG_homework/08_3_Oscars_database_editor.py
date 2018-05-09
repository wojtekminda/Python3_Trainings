'''
Building upon 'What did they win their Oscars for?' exercise, create an interactive editor of the awards file.
The session with the script is as follows:
1.The awards file is read into memory as a list of dictionaries.
2.The number of entries is printed to the screen.
3.The user is repeatedly asked to provide a command. If the user entered:
• add, the script asks for details (category, actor, title and date) and appends a new dictionary to the end of the list
• remove, the script asks for actor's full name and marks all the dictionaries with that actor for removal
(e.g. adds 'remove' key to them)
• cancel, the script ends
• confirm, the scripts overwrites the awards file with the data coming from the list of dictionaries
(skipping those marked for removal). The script ends.
• anything else: nothing happens and user is asked to provide a recognizable command again.

Remember to use identical format when overwriting the file.
(one award per line, fields separated by tabs in the well defined order)

Provide your own modifications, as you please. For example, you could provide a more sensible remove command,
so that the user is able to remove a specific award and not all the awards for the given actor.
'''

file = '.\\08_Best_actor_and_actress_DB\\best_actor_and_actress_db'

list_of_dict = []
with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        dict = {}
        line = line.split('\t')
        line[3] = line[3].strip()
        dict['category'] = line[0]
        dict['actor'] = line[1]
        dict['title'] = line[2]
        dict['date'] = line[3]
        list_of_dict.append(dict)

print('The database contains', len(list_of_dict), 'awards.')

while True:
    command = input('Please, provide a command (add/remove/confirm/cancel): ')

    if command == "add":
        dict = {}
        dict['category'] = input('Please, provide category (M/F): ')
        dict['actor'] = input('Please, provide name: ')
        dict['title'] = input('Please, provide title: ')
        dict['date'] = input('Please, provide date: ')
        list_of_dict.append(dict)

    elif command == 'remove':
        to_remove = input('Please, provide the name of actor you want to remove: ')
        for item in list_of_dict:
            if item['actor'] == to_remove:
                item['remove'] = True

    elif command == 'confirm':
        with open(file, 'w', encoding='utf-8') as f:
            for item in list_of_dict:
                if 'remove' not in item:
                    f.write(item['category'])
                    f.write('\t')
                    f.write(item['actor'])
                    f.write('\t')
                    f.write(item['title'])
                    f.write('\t')
                    f.write(item['date'])
                    f.write('\n')
        print('Database updated...')
        break

    elif command == 'cancel':
        print('All operations cancelled...')
        break

    else:
        print('Wrong command...')
