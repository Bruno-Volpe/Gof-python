from abc import ABC. abstractmethod     

class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo esta buscando o cliente')


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular esta buscando o cliente')


class VeiculoFactory:
    @staticmethod
    def get_carro(tio: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        else:
            return CarroPopular()


if __name__ == '__main__':
    from random import choice
    carros_disponiveis = [
        'luxo',
        'popular'
    ]

    for c in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()