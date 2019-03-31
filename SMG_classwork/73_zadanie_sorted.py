def sort_by_title(movies):
    movies.sort(key=get_title)

def get_title(movie):
    return movie['title']

movies = [
    {'title': 'bob', 'actor': 'b'},
    {'title': 'alice', 'actor': 'a'},
    {'title': 'damian', 'actor': 'd'},
    {'title': 'charlie', 'actor': 'c'}
]
print(movies)

sort_by_title(movies)
print(movies)
