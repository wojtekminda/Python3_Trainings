def modify(stuff, thing):
    stuff = list(stuff) # copy the provided list and forget it
    stuff.append(thing) # append to the copy
    return stuff        # return the new list

names = ['Alice', 'Bob']
new_names = modify(names, 'Charlie')
print(names)        # prints: ['Alice', 'Bob']
print(new_names)    # prints: ['Alice', 'Bob', 'Charlie']
