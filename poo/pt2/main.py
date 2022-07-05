from init import Escritor
from init import Caneta
from init import Machine
from init import People
from init import Student
from init import AA, abstractmethod
from init import erroError

escritor = Escritor('Jooj')
print(escritor.name)

caneta = Caneta('Bic')
print(caneta.logo)

machine = Machine('AA')
print(machine.nameMachine)

people = People('Charles', 20)
student = Student('Charles', 20)
#student.speak('aa')


erroError.teste(':()')
