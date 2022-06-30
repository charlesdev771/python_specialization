def show_menu(jooj = 'Jooj'):
    print(f'Jooj {jooj}')
    msg = jooj.replace('o', 'AA')
    print(msg)

show_menu('aa')
show_menu(jooj = 'aaaaa')

def teste1(teste):
    print('aa')

def teste2():
    return teste1

var = teste2()('Gogogo')
print(var)

def args(*args):
    print(args)

print(args(1,2,3,4,5,5))

#global variavel = '123'

a = lambda x, y: x * y #lambda
print(a(12,21))
