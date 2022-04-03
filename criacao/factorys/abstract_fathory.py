from abc import ABC. abstractmethod


class VeiculoLuxo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class VeiculoPopular(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxoZN(VeiculoLuxo):

    def buscar_cliente(self) -> None:
        print('Carro de luxo de ZN esta buscando o cliente')


class CarroPopularZN(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular de ZN esta buscando o cliente')


class CarroLuxoZS(VeiculoLuxo):
    def buscar_cliente(self) -> None:
        print('Carro de ZS luxo esta buscando o cliente')


class CarroPopularZS(VeiculoPopular):
    def buscar_cliente(self) -> None:
        print('Carro popular de ZS esta buscando o cliente')


class VeiculoFactory(ABC):
    @staticmethod
    @abstractmethod
    def get_carro_popular() -> VeiculoPopular: pass

    @staticmethod
    @abstractmethod
    def get_carro_luxo() -> VeiculoLuxo: pass


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: pass:
        return CarroPopularZN()

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: pass:
        return CarroLuxoZN()


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro_popular() -> VeiculoPopular: pass:
        return CarroPopularZS()

    @staticmethod
    def get_carro_luxo() -> VeiculoLuxo: pass:
        return CarroLuxoZS()


class Cliente:
    def busca_clientes(self):
        for factory in [ZonaNorteVeiculoFactory(), ZonaSulVeiculoFactory()]:
            carro_popular = factory.get_carro_popular()
            carro_popular.buscar_cliente()

            carro_luxo = factory.get_carro_luxo()
            carro_luxo.buscar_cliente()


if __name__ == '__main__':
    from random import choice

    cliente = Cliente()
    cliente.busca_clientes()
