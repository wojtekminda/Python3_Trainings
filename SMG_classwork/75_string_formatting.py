# https://pyformat.info/

# https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
old_formatting = '%s %s' % ('one', 'two')
print(old_formatting)

# https://docs.python.org/3/library/string.html#formatstrings
new_formatting = '{} {}'.format('three', 'four')
print(new_formatting)
