"""
Tem a itencao de fazer um 'backup'
"""
from abc import ABC, abstractmethod
from copy import deepcopy

class Memento:
    def __init__(self, state) -> None:
        self._state
        super().__setattr__('_state', state)
    
    def get_state(self) -> dict:
        return self._state
    
    def __setattr__(self, name, value):
        raise AttriubuteError('Sorry sou imutavel')


class ImageEditor:
    def __init__(self, name, widht, height):
        self.name = name
        self.widht = widht
        self.height = height
    
    def save_state(self):
        return Memento(deepcopy(self.__dict__))

    def restore(self memento):
        self.__dict__ = memento.get_state()


class CareTaker:
    def __init__(self, originator):
        self._originator = originator
        self._mementos = []

    def backup(self):
        self._mementos.append(self._originator.save_state())
    
    def restore(self):
        if not self.mementos:
            return
        
        self._originator.restore(self.mementos.pop())


if __name__ == "__main__":
    pass 