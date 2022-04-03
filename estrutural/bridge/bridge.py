"""
Bridge é um padrão de projeto estrutural que
tem a intenção de desacoplar uma abstração
da sua implementação, de modo que as duas
possam variar e evoluir independentemente.

Abstração é uma camada de alto nível para algo.
Geralmente, a abstração não faz nenhum trabalho
por conta própria, ela delega parte ou todo o
trabalho para a camada de implementação.

RELEMBRANDO: Adapter é um padrão de projeto
estrutural que tem a intenção de permitir
que duas classes que seriam incompatíveis
trabalhem em conjunto através de um "adaptador".

Diferença (GOF pag. 208) - A diferença chave
entre esses padrões está nas suas intenções...
...O padrão Adapter faz as coisas funcionarem
APÓS elas terem sido projetadas; o Bridge as
faz funcionar ANTES QUE existam...
"""
from abc import ABC, abstractmethod

class IRemoteControl(ABC):
    @abstractmetod
    def increase_volume(self) -> None: pass

    @abstractmetod
    def decrease_volume(self) -> None: pass

    @abstractmetod
    def power(self) -> None: pass


class RemoteControl(IRemoteControl):
    def __init__(self, device) -> None:
        self.device = device

    def increase_volume(self) -> None:
        self.device.volume += 10

    def decrease_volume(self) -> None:
        self.device.volume -= 10

    def power(self) -> None: pass
        self.device.power = not self.device.power

class IDevice(ABC):
    @property
    @abstractmethod
    def volume(self) -> int: pass

    @volume.setter
    def volume(self, volume): pass

    @property
    @abstractmethod
    def power(self) -> bool: pass

    @power.setter
    def power(self, power): pass


class TV(IDevice):
    def __init__(self)
        self.volume = 10
        self.power = False

    @property
    def volume(self) -> int: 
        return self.volume

    @volume.setter
    def volume(self, volume):
        if not self.power:
            print('Nao esta ligado')
            return
        if volume > 100:
            return

        if volume < 0:
            return

        self.volume = volume

    @property
    def power(self) -> bool:
        return self.power

    @power.setter
    def power(self, power):
        self.power = power