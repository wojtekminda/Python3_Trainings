names = ('Emma', 'Charlie', 'Debbie', 'Alice', 'Fred', 'Bob')

def last_letter(name):
    return name[-1]

sorted_list = sorted(names, key=last_letter)
print(sorted_list)

sorted_list = sorted(names, key=len)
print(sorted_list)
