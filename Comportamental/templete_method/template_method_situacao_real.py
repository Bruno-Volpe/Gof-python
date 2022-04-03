from abc import ABC, abstractmethod


class Pizza(ABC):
    """ Classe abstrata """

    def prepare(self):  # Template Method
        self.add_ingredients()
        self.cook()
        self.serve()

    @abstractmethod
    def add_ingredients(self): pass

    @abstractmethod
    def cook(self): pass

    def serve(self):  # Hook
        print('Servindo pizza')


class AModa(Pizza):

    @abstractmethod
    def add_ingredients(self):
        print('A moda: Presunto e queijo')

    @abstractmethod
    def cook(self):
        print('Cozinhar por 50 min')


if __name__ == "__main__":
    amoda = AModa()
    amoda.prepare()
