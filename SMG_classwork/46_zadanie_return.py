def get_year(date):
    #return int(date.split(',')[1])
    return int(date[-4:])

year = get_year('March 7, 2018')
print(year)

print(get_year('March 7, 2018') * 2)
