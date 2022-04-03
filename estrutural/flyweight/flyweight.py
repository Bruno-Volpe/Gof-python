"""
Flyweight é um padrão de projeto estrutural
que tem a intenção de usar compartilhamento
para suportar eficientemente grandes quantidades
de objetos de forma granular.

Só use o Flyweight quanto TODAS as condições
a seguir forem verdadeiras:

- uma aplicação utiliza uma grande quantidade de
objetos;
- os custos de armazenamento são altos por causa
da grande quantidade de objetos;
- a maioria dos estados de objetos podem se tornar
extrínsecos;
- muitos objetos podem ser substituídos por poucos
objetos compartilhados;
- a aplicação não depende da identidade dos objetos.

Importante:
- Estado intrínseco é o estado do objeto que não muda,
esse estado deve estar dentro do objeto flyweight;
- Estado extrínseco é o estado do objeto que muda,
esse estado pode ser movido para fora do objeto
flyweight;

Dicionário:
Intrínseco - que faz parte de ou que constitui a
essência, a natureza de algo; que é próprio de
algo; inerente.
Extrínseco - que não pertence à essência de algo;
que é exterior.
"""
from abc import ABC, abstractmethod
from __future__ import annotations

class Client():
    """ Context """

    def __init__(self, name: str) -> None:
        self._name: str = name
        self._adresses: list = []

        # Extrinscs adress data
        self._adrress_number: str
        self._adrress_detail: str

    def add_adress(self, adress) -> None:
        self._adresses.append(adress)

    def list_adresses(self):
        for adress in self._adresses:
            adress.show_adress(self._adress_number, self._adrress_detail)


class Adress:
    """ Flyweight """
    def __init__(self, street, neighbourhood, zip_code) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_adress(self, adress_number, adress_details):
        print(f'{self.street} {adrees_number} {selfneighboorrood} ...')

    
class AdressFactory:
    _adresses: dict = {}

    def get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_adress(**kwargs):
        key = self.get_key(**kwargs):

        try:
            adress_flyweight = self.adresses[key]
        except KeyError:
            addres_flyweight = Adress(**kwargs)
            self._adrres[key] = adress_flyweight

            return addres_flyweight