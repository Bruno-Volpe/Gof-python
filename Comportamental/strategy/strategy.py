""""
Stategy eu um padrao comportamental que tem a intencao de definir uma familia
de algoritimos, encapsular cada uma delas e torna-las intercambiadas

Principio: Open, Close, S.O.L.I.D (uncle bob)
Entidades devem ser abertas para extensao, mas fechadas para modificacoes
"""
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total, discount):
        self.total = total
        self.discount = discount

    @property
    def total(self):
        return self.total

    @property
    def total_with_doscount(self):
        return self.discount.calculete(self.total)

# Estrategia de desconto, ou seja aqui se usa o GoF: Strategy


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value) -> float: pass


class TwentyPercent(DiscountStrategy):
    def calculate(self, value) -> float:
        return value - (value * 0.2)


if __name__ == "__main__":
    twentyPercent = TwentyPercent()

    order = Order(1000, twentyPercent)
