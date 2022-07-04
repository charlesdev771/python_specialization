from random import randint
class Pessoa:

    year = 2022


    def __init__(self, name, age, price):
        self.name = name
        self.age = age
        self.price = price

    def speeak(self):
        print(f' the {self.name} speaking: aa')

    @staticmethod
    def generate_id():
        rand = randint(10, 100)
        return rand



    @property

    def name(self):
        return self._name

    @name.setter
    def name(self, nameM):
        if isinstance(nameM, str):
            nameM = nameM.replace('', '')
        self._name = nameM

    #getter
    @property
    def price(self):
        return self._price

    #setter
    @price.setter
    def price(self, valor):
        if isinstance(valor, str):
            valor = valor.replace('R$', '')
        self._price = valor


        



p1 = Pessoa('Charles', 20, 30)
p1.speeak()
print(p1.name)

print(Pessoa.generate_id())
print(p1.generate_id())
