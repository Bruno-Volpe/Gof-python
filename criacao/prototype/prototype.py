"""
Especificar os tipos de objetos a serem criados
usando uma instancia-prototipo e criar novos objeto pela copia
desse prototipo
"""


class Person:
    def __init__(self, firstname, lastname) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.adresses = []

    def add_adress(self, adress):
        self.adresses.append(adress)


class Adress:
    def __init__(self, street, number) -> None:
        self.street = street
        self.number = number


if __name__ == "__main__":
    from copy import deepcopy

    bruno = Person('Bruno Volpe')
    enderco_bruno = Adress('End', '123')
    bruno.add_adress(enderco_bruno)

    # Daria errado, ja que a esposa alteraria o valor de bruno tb
    esposa_bruno = bruno
    esposa_bruno.firstname = 'nina'

    # Agora sim
    esposa_bruno = deepcopy(bruno)
    esposa_bruno.firstname = 'nina'
