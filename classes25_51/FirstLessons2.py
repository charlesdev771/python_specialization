variable1 = input("Number one: ")
variable2 = input('Number two: ')
name = 'Chameleon'
if not variable1 > variable2:

    print("aa")


else:

    print('BB')

if 'a' in name:

    print('Jooj')

size_of_variable = name.__len__() #len()
print(size_of_variable, name, type(size_of_variable))

#isnumeric, isdigit, isdecimal
#print(variable1.isnumeric())

if variable1 == True:
    pass #...
else:
    print('Dont pass {n}'.format(n=variable1))

name = name.ljust(20, '#')
print(name.lower())
print(name.upper())
print(name.title())
print(name[7])
print(name[-1])

x = 1

while x <= 100:
    print(x)
    x+=1
    if x == 10:
        continue
else:
    print('end loop')
