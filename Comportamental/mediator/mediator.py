"""
Nao eh muito famoso, nem uitlizado, mas...

Tem a itencao de definir um objeto que
encapsula a forma como um conjunto de objetos 
interage. O mediator promove o baixo acoplamento
"""
from abc import ABC, abstractmethod


class Colleague(ABC):
    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None: ...

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def show(self, collegue, msg): pass

    def direct(self, sender, msg, receiver): pass


class ChatRoom(Mediator):
    def __init__(self):
        self.collegues = []

    def add_collegue(self, collegue):
        if not collegue in self.collegues:
            self.collegues.append(collegue)

    def show(self, collegue, msg):
        print(f'mandando sms')

    def direct(self, sender, msg, receiver):
        recever_obj = [for colleague in self.collegues
                       if collegue.name == name
                       ]
