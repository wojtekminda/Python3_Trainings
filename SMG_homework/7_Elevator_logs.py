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
start_date = '2018-02-08'
end_date = '2018-02-12'

start_date_int = int(start_date.split('-')[0])*366 + int(start_date.split('-')[1])*31 + int(start_date.split('-')[2])
end_date_int = int(end_date.split('-')[0])*366 + int(end_date.split('-')[1])*31 + int(end_date.split('-')[2])
print('Start date:', start_date, '->', start_date_int)
print('End   date:', end_date, '->', end_date_int)
print()

path = '.\\7_Elevator_logs_FILES\\logs.txt'
start_floor = 0
distances = []
with open(path, encoding='utf-8') as f:
    for line in f:
        date = line.split()[0]
        date_int = int(date.split('-')[0])*366 + int(date.split('-')[1])*31 + int(date.split('-')[2])
        if date_int >= start_date_int and date_int <= end_date_int:
            floors = line.split()[1:]
            print('Date:', date, '->', date_int, '| Start floor:', start_floor, '| Floors:', floors)
            for floor in floors:
                dist = abs(int(start_floor) - int(floor))
                distances.append(dist)
                start_floor = floor
        start_floor = line.split()[-1]

print('\nDistances:', distances)
print('The elevator went through', sum(distances), 'floors in that period.')
