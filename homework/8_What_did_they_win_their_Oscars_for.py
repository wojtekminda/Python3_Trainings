'''
Write a script which works with a textual database file (use best_actor_and_actress_db).

About best_actor_and_actress_db:
best_actor_and_actress_db is a database of Academy Awards in Best Actor and Best Actress categories,
received between 1929 and 2016. It is a text file in UTF-8 encoding. Each line of the file describes one award.
Each line consists of four fields. Fields are separated by single tab characters ('\t'),
i.e. there are 3 tab characters per line. The fields in every line are, in order:
1.category ("M" for Best Actor and "F" for Best Actress),
2.winner's full name,
3.title of the movie,
4.date in the format: Month Day, YYYY (contains two space characters).

Note that, except for category, every field may and often does contain space characters.

The script should:
1.Read and analyze the file as a list of dictionaries.
Each dictionary describes one award and contains 4 keys (such as 'category', 'actor', 'title', 'date').
The values in the dictionary come from a single line in the file.
2.Display the total number of awards (i.e. the number of lines or the length of the list of dictionaries).
3.Ask for an actor's full name.
4.Display number of matching records (with that actor or actress).
5.Display a list of movies for which this actor was awarded.
This should be a list of titles, each separated by semicolon followed by space ('; ').

Example session with the script:
The database contains 178 awards.
Enter an actor's or actress' full name: Meryl Streep
This person won 2 awards for the following movies:
Sophie's Choice; The Iron Lady
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

actor = input('Enter an actor\'s or actress\' full name: ')
#actor = 'Meryl Streep'

list_of_title = []
for item in list_of_dict:
    if item['actor'] == actor:
        print(item)
        list_of_title.append(item['title'])

print('This person won', len(list_of_title), 'awards for the following movies:\n' + '; '.join(list_of_title))
