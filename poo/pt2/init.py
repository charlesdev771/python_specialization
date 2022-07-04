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
