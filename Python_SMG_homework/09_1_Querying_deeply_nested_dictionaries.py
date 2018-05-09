'''
Write a function called fetch() which takes two arguments:
1. A dictionary. This dictionary may have other nested dictionaries (see example below).
2. A string which is path of keys in the dictionary. Path components are separated by dots.

The function returns value assigned to the last key on the path.

You may use the following sample deeply nested dictionaries:

SOLAR_SYSTEM = {
    'planets': {
        'Mercury': { 'mass': 0.055, 'year': 87.9691 },
        'Venus': { 'mass': 0.815, 'year': 224.701 },
        'Mars': {
            'mass': 0.107,
            'year': 686.971,
            'moons': {
                'Phobos': {'mass': 0.000000001785},
                'Deimos': {'mass': 0.000000000247}
            }
        }
    },
    'units': {'mass': 'Earth masses', 'year': 'Earth days'}
}

In this case, consider this code snippet:
year = fetch(SOLAR_SYSTEM, 'planets.Venus.year')
unit = fetch(SOLAR_SYSTEM, 'units.year')
print(year, unit)  # prints: 224.701 Earth days

The function may ignore any errors resulting from incorrect object types or missing keys:
fetch(SOLAR_SYSTEM, 'planets.Venus.volume')       # KeyError
fetch(SOLAR_SYSTEM, 'planets.Venus.year.length')  # TypeError

As an additional challenge, add support for lists. If a path component consists of digits only,
assume the object being indexed is a list and convert the component to a number.
isdigit() string method might prove useful.
'''

def fetch(nested_dictionary, path_of_keys):
    path_of_keys_list = path_of_keys.split('.')
    for key in path_of_keys_list:
        if key in nested_dictionary:
            nested_dictionary = nested_dictionary[key]
        else:
            return 'There are no such item!'
    return nested_dictionary

SOLAR_SYSTEM = {
    'planets': {
        'Mercury': {
            'mass': 0.055,
            'year': 87.9691},
        'Venus': {
            'mass': 0.815,
            'year': 224.701},
        'Mars': {
            'mass': 0.107,
            'year': 686.971,
            'moons': {
                'Phobos': {'mass': 0.000000001785},
                'Deimos': {'mass': 0.000000000247}
            }
        }
    },
    'units': {
        'mass': 'Earth masses',
        'year': 'Earth days'
    }
}

mass = fetch(SOLAR_SYSTEM, 'planets.Mercury.mass')
unit = fetch(SOLAR_SYSTEM, 'units.mass')
print('Planet mass:', mass, unit)

year = fetch(SOLAR_SYSTEM, 'planets.Venus.year')
unit = fetch(SOLAR_SYSTEM, 'units.year')
print('Year duration:', year, unit)

mass = fetch(SOLAR_SYSTEM, 'planets.Mars.moons.Deimos.mass')
unit = fetch(SOLAR_SYSTEM, 'units.mass')
print('Moon mass:', mass, unit)

print(fetch(SOLAR_SYSTEM, 'planets.Venus.volume'))

fetch(SOLAR_SYSTEM, 'planets.Venus.year.length')    # TypeError
