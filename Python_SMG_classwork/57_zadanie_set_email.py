def set_email(email, user=None):
    if user == None:
        user = dict()
    user['email'] = email
    return user

user = {'username': 'foo'}
print(user)     # prints: {'username': 'foo'}

user1 = set_email('x@example.com')
user2 = set_email('y@example.com')
user3 = set_email('foo@example.com', user)

print(user1)    # prints: {'email': 'x@example.com'}
print(user2)    # prints: {'email': 'y@example.com'}
print(user3)    # prints: {'username': 'foo', 'email': 'foo@example.com'}
print(user)     # prints: {'username': 'foo', 'email': 'foo@example.com'}
