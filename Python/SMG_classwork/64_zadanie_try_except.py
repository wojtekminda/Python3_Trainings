def dateParser(date):
    date = date.split('-')

    if not date[0].isdigit():
        raise ValueError('wrong form of year element')
    year = int(date[0])

    if not date[1].isdigit():
        raise ValueError('wrong form of month element')
    month = int(date[1])

    if not date[2].isdigit():
        raise ValueError('wrong form of day element')
    day = int(date[2])

    if len(date) != 3:
        raise ValueError('not proper number of date elements')
    if len(date[0]) != 4:
        raise ValueError('not proper form of year element')
    if month > 12 or month < 1:
        raise ValueError('wrong number of months')
    if day > 31 or day < 1:
        raise ValueError('wrong number of days')
    return year, month, day

date = input('Provide a date to parse: ')
while date:
    try:
        parsedDate = dateParser(date)
        print(parsedDate)
    except ValueError as exc:
        print('Exception: ', exc)
    except TypeError:
        print('TypeError!')
    date = input('Provide a date to parse: ')
