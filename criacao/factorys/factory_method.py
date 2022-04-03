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


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro(tio: str) -> Veiculo: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    def get_carro(tio: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroLuxo()
        else:
            return CarroPopular()


class ZonaSulVeiculoFactory(VeiculoFactory):
    def get_carro(tio: str) -> Veiculo:
        if tipo == 'luxo':
            return CarroPopular()
        else:
            return 'Estamos sem carros de luxos no momento'


if __name__ == '__main__':
    from random import choice

    veiculos_disponiveis_zona_norte = [
        'luxo',
        'popular'
    ]
    veiculos_disponiveis_zona_sul = [
        'popular'
    ]

    for c in range(10):
        carro = ZonaNorteVeiculoFactory.get_carro(
            choice(veiculos_disponiveis_zona_norte))
        carro.buscar_cliente()

        carro2 = ZonaSulVeiculoFactory.get_carro(
            choice(veiculos_disponiveis_zona_sul))
        carro2.buscar_cliente()
