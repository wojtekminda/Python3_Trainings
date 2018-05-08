columns = ('cat', 'actor', 'title')

def make_award(row):
    return dict(zip(columns, row))

award = make_award(['M', 'Anthony Hopkins', 'Silence of the Lambs'])

print(award)
