def parenthesis_check(text):
    start_counter = 0
    stop_counter = 0
    for sign in text:
        if sign == '(':
            start_counter = start_counter + 1
        elif sign == ')':
            stop_counter = stop_counter + 1
            if stop_counter > start_counter:
                return False
    return start_counter == stop_counter

print(parenthesis_check('(test)'))
print(parenthesis_check(')test('))
print(parenthesis_check('((test)'))
print(parenthesis_check('(test))'))
print(parenthesis_check('((()test))'))
