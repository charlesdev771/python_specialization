name = 'chameleon'
name_len = len(name)
c = 0

while c <= len(name):
    print(name)
    c+=1

for letter in name:
    print(letter)

for i in range(10):
    print(i)

for n in range(1,60, 5):
    print(n)

#pop, insert, del(lisT[3:5])m appendm, startswitch
lisT = [1,2,3,14,'AA', 'jooj']
print(lisT[0:5])
print(lisT[::2])
lisT.insert(0, 'CC')
print(lisT)
l2 = list(range(1,15))
print(l2)

for names in name:
    print(name)
else:
    print('Not')

string = 'Charles Dantas'
string2 = string.split(' ')
print(string2)

for v1, v2 in enumerate(string2):
    print(v1, v2)

logged_user = False
msg = 'Logged' if logged_user else "No logged"
print(msg)
