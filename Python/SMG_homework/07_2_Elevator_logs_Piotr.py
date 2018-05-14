'''
Whenever an elevator stops on a floor, it writes the floor number into a log file. Each day has its own line in the log file.
Every line starts with a date in YYYY-MM-DD format.
Then, separated by spaces, there follow floor numbers on which the elevator stopped on that day.
Lines in the log file are sorted by date in ascending order. Consider this example log file:
2018-02-07 5 15 1 7
2018-02-08 8 9 5 4 1
2018-02-09 13 14 1
2018-02-10 4 2 10 7 15 13 1
2018-02-11 8 3 2
2018-02-12 1 13 1 15 9

Write a script which analyzes the log file and:
- asks the user for a start date (inclusive),
- asks the user for an end date (inclusive),
- prints the distance (expressed in the number of floors) the elevator traveled in that period.

The following example is for the sample log file shown above.
Start date (YYYY-MM-DD): 2018-02-09
End date (YYYY-MM-DD): 2018-02-11
The elevator went through 77 floors in that period.

Note that, even though the period is between Feb, 9 and Feb, 11, we have to consider the last floor on Feb, 8.
'''

#start_date = input('Start date: [YYYY-MM-DD]: ')
#end_date = input('End date:   [YYYY-MM-DD]: ')
start_date = '2018-02-09'
end_date = '2018-02-11'

# PC: Obawiam sie, ze ta formula nie jest poprawna. Dziala tylko dlatego, ze
#     w przykladowym pliku daty roznia sie jedynie dniami (rok i miesiac wszedzie sa
#     takie same). Jezeli chciales przeksztalcic date na liczbe dni od roku 1, to raczej:
#         year * 365 + month * 30 + day
#     Ale wciaz: nie kazdy rok ma 365 dni i nie kazdy miesiac ma ich 30, wiec nie jest
#     to niestety takie proste.
#
#     Odsylam natomiast do podpowiedzi z zadania:
#         If dates are stored as strings in YYYY-MM-DD format, it is enough to
#         compare them lexicographically using ordering operators such as <.
#     Tzn. np.: "2018-02-28" < "2018-03-01" zwraca True, bo tak wynika z logiki porownywania
#     stringow, a przy okazji jest to rowniez poprawne uporzadkowanie dat.
start_date_int = int(start_date.split('-')[0])*365 + int(start_date.split('-')[1])*12 + int(start_date.split('-')[2])
end_date_int = int(end_date.split('-')[0])*365 + int(end_date.split('-')[1])*12 + int(end_date.split('-')[2])
print('Start date:', start_date, '->', start_date_int)
print('End   date:', end_date, '->', end_date_int)
print()

path = '.\\07_Elevator_logs_FILES\\logs.txt'
start_floor = 0
distances = []
with open(path, encoding='utf-8') as f:
    for line in f:
        # PC: wszedzie powtarza sie to line.split(), to juz mozna bylo napisac:
        #         line = line.split()
        date = line.split()[0]
        date_int = int(date.split('-')[0])*365 + int(date.split('-')[1])*12 + int(date.split('-')[2])
        # PC: O tym nie mowilem, ale w takich sytuacjach wygodny jest ten nietypowy element
        #     skladni Pythona:
        #         if start_date_int <= date_int <= end_date_int:
        if date_int >= start_date_int and date_int <= end_date_int:
            floors = line.split()[1:]
            print('Date:', date, '->', date_int, '| Start floor:', start_floor, '| Floors:', floors)
            for floor in floors:
                dist = abs(int(start_floor) - int(floor))
                distances.append(dist)
                # PC: Milo by bylo, gdyby start_floor nigdy nie byla stringiem.
                #     Nie musielibysmy konwertowac kazdej liczby dwukrotnie!
                start_floor = floor
        # PC: Ponizsza linijka moglaby znalezc sie w elsie, bo jezeli warunek jest spelniony,
        #     to petla for juz zadbala o ustawienie start_floor.
        start_floor = line.split()[-1]

print()
# PC: Oczywiscie gdybys nie potrzebowal drukowac listy, moglbys w ogole jej nie tworzyc
#     a tylko na biezaco obliczac sume.
print('Distances:', distances)
print('The elevator went through', sum(distances), 'floors in that period.')
