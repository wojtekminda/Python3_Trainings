def truncate(text, words=7):
    text = text.split()
    if len(text) <= words:
        return ' '.join(text)
    return ' '.join(text[:words]) + '...'

print(truncate('Ala ma kota, a kot ma ale. Ale kogo to obchodzi.'))
print(truncate('Ala ma kota, a kot ma ale. Ale kogo to obchodzi.', 4))
print(truncate('Ala ma kota, a kot ma ale. Ale kogo to obchodzi.', 40))
