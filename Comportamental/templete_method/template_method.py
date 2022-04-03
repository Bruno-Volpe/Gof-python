"""
Template Method tem a intencao de definir um algoritimo em um metodo 
postergando algins passos para as subclasses por hernca
"""
# Implementacao do Gof puro
from abc import ABC, abstractmethod


class Abstract(ABC):
    # Nao pode ser abstrato e nao deve ser reescrito pelas subclasses
    def templete_method(self):
        self.hook()
        self.operation1()
        self.operation2()

    def hook(self): pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass


class ConcreteClass(Abstract):
    def hook(self):
        print('Fui reescrito, porem nao eh obrigatorio me reescrever')

    @abstractmethod
    def operation1(self):
        print('Operacao 1')

    @abstractmethod
    def operation2(self):
        print('Operacao 2')


if __name__ == "__main__":
    concrete_class_1 = ConcreteClass()
    c1.template_method()  # Principio hollywood - Nao nos chame, nos o chamaremos
