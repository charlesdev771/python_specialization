class Escritor:

    def __init__(self, name):
        self.__name = name


    @property
    def name(self):
        return self.__name


class Caneta:
    def __init__(self, logo):
        self.__logo = logo

    @property
    def logo(self):
        return self.__logo

class Machine:

    def __init__(self, nameMachine):
        self.__nameMachine = nameMachine

    @property
    def nameMachine(self):
        return self.__nameMachine

###########################################

class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak():
        print('aa')

#class Student(People):
#    def speak(self, aa):
#        super().speak()
#        print('bb')


#################################


class erroError(Exception):

    def teste():
        raise erroError(': ()')

class Magic:

    def __new__(self, *args, **kwargs):
        pass

    def __init__(self):
        print('aa')

print(a = Magic())
