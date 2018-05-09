'''
Imagine a textual database file in which columns are fixed-width and have no separators. For example:

Mariner 4                  1964-11-28USA          Flyby         Successful
Rosetta                    2004-03-02Europe       Gravity assistSuccessful
Mars Reconnaissance Orbiter2005-08-12USA          Orbiter       Operational
ExoMars Trace Gas Orbiter  2016-03-14Europe/RussiaOrbiter       Operational

Write parse_row() function which, given a row from the table as a string and a sequence of column widths,
returns a list of individual values with surrounding white-space stripped:

COL_WIDTHS = [27, 10, 13, 14, 11]
L1 = "Mariner 4                  1964-11-28USA          Flyby         Successful "
L2 = "ExoMars Trace Gas Orbiter  2016-03-14Europe/RussiaOrbiter       Operational"

# prints: ['Mariner 4', '1964-11-28', 'USA', 'Flyby', 'Successful']
print(parse_row(L1, COL_WIDTHS))

# prints: ['ExoMars Trace Gas Orbiter', '2016-03-14', 'Europe/Russia', 'Orbiter', 'Operational']
print(parse_row(L2, COL_WIDTHS))

# prints: ['alice', 'bob', 'charlie']
print(parse_row("alicebobcharlie", (5, 3, 7))
'''

def parse_row(to_parse, widths):
    start_pointer = 0
    columns = []
    for width in widths:
        column = to_parse[start_pointer:start_pointer + width]
        start_pointer = start_pointer + width
        column = column.rstrip()
        columns.append(column)
    return columns

COL_WIDTHS = [27, 10, 13, 14, 11]
L1 = "Mariner 4                  1964-11-28USA          Flyby         Successful "
L2 = "ExoMars Trace Gas Orbiter  2016-03-14Europe/RussiaOrbiter       Operational"

# prints: ['Mariner 4', '1964-11-28', 'USA', 'Flyby', 'Successful']
print(parse_row(L1, COL_WIDTHS))

# prints: ['ExoMars Trace Gas Orbiter', '2016-03-14', 'Europe/Russia', 'Orbiter', 'Operational']
print(parse_row(L2, COL_WIDTHS))

# prints: ['alice', 'bob', 'charlie']
print(parse_row("alicebobcharlie", (5, 3, 7)))
