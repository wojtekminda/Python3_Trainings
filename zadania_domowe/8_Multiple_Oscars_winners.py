'''
Analyze best_actor_and_actress_db file and list all actor/actress' names from the database accompanied by the number of awards they received.
Skip actors/actresses who won only one award. See 'What did they win their Oscars for?' exercise for the description of the database file.
You may also follow implementation from that exercise (analyze the file as a list of dictionaries), but you may write a simpler implementation, too.
'''

file = '.\\8_Best_actor_and_actress_DB\\best_actor_and_actress_db'

list_of_dict = []
with open(file, encoding='utf-8') as f:
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

counters = {}
for item in list_of_dict:
    actor = item['actor']
    if actor in counters:
        number = counters[actor]
        number = number + 1
        counters[actor] = number
    else:
        counters[actor] = 1

for key in counters:
    if counters[key] > 1:
        print(key + ': ' + str(counters[key]))
