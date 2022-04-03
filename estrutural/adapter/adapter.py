"""
Tem a itencao de permitir que 2 classes 
que seriam incompativeis, se tornarem compativeis
"""
from abc import ABC, abstractmethod


class Icontrol(ABC):
    @abstractmethod
    def top(self): pass

    @abstractmethod
    def down(self): pass

    @abstractmethod
    def right(self): pass

    @abstractmethod
    def left(self): pass

class Control(ABC):
    def top(self):
        print('Movendo para cima')

    def down(self):
        print('Movendo para baixo')

    def right(self):
        print('Movendo para direita')

    def left(self): 
        print('Movendo para esquerda')

    
class NewControl:
    def move_top(self):
        print('Movendo para cima')

    def move_down(self):
        print('Movendo para baixo')

    def move_right(self):
        print('Movendo para direita')

    def move_left(self): 
        print('Movendo para esquerda')


class Adpter:
    def __init__(self, new_control):
        self.new_control = new_control
    
   def top(self):
        self.new_control.move_top()

    def down(self):
        self.new_control.move_down()

    def right(self):
        self.new_control.move_right()

    def left(self): 
        self.new_control.move_left()



if __name__ == "__main__":
    c1 = NewControl()
    c1_adpter = Adpter(c1)

    c1_adpter.up()
