with open('data/test.txt') as file:
    data = file.read()

displayed = ''
for word in data:
    displayed += word

print(displayed)
