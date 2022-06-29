from random import randint

number = randint(100, 9999)

name = input('Name: ')
if name:
    print(name)
else:
    print('AA :(')

print(name or 'AAAAAAAAAAAAa : ()')

print(number)
