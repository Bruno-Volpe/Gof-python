from abc import ABC, abstractmethod
from __future__ import annotations


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self): pass

    @abstractmethod
    def get_price(self): pass

    def add(self,child): pass

    def remove(self, child): pass


class Box(BoxStructure):
    def __init__(self, name) -> None:
        self.name = name
        self._children: List[boxStructure]

    def print_content(self): pass
        for child in self._children:
            child.print_content()

    def get_price(self): pass
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self,child): 
        self._children.append(child)

    def remove(self, child):
        if child in self.children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_content(self): 
        print(self.name, self.price)

    def get_price(self):
        return self.price

if __name__ == "__main__":
    # Leaf
    camiseta1 = Product('camiseta1', 10)
    camiseta2 = Product('camiseta2', 10)
    camiseta3 = Product('camiseta3', 10)

    # Composite
    caixa_camisetas = Box('Caixa de camiseta')
    caixa_camisetas.add(camiseta1)
    caixa_camisetas.add(camiseta2)
    caixa_camisetas.add(camiseta3)

    # Leaf
    smartphone1 = Product('smartphone1', 10000)
    smartphone2 = Product('smartphone2', 10000)

    # Composite
    caixa_smartphones = Box('Caixa de Smartphones')
    caixa_smartphones.add(smartphone1)
    caixa_smartphones.add(smartphone2)

    # Composite
    caixa_grande = Box('Caixa grande')
    caixa_grande.add(caixa_camisetas)
    caixa_grande.add(caixa_smartphones)
    caixa_grande.print_content()
    print(caixa_grande.get_price())