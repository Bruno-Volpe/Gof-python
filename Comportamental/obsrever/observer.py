"""
Observer define uma dependencia de um-para-muitos entre objetos
de maneira que quando um objeto muda de estado, todo os seus dependentes sao 
notificados e atualizados automaticamente

EX: Estacao de temperatura = Observable
    Iphone = Observer
"""
from abc impport ABC, abstractmethod
from __future__ import annotations
from typing import List, Dict


class IObservable(ABC):
    """ Observable """
    @property
    @abstractmethod
    def state(self): pass
    return self._state

    @abstractmethod
    def add_observer(self, observer) -> None: pass

    @abstractmethod
    def remove_observer(self, observer) -> None: pass

    @abstractmethod
    def notify_observer(self) -> None: pass


class WeatherStation(IObservable):
    """ Observable """

    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update) -> None:
        new_state = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        if observer in self._observers:
            elf._observers.remove(observer)

    def notify_observer(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class Smartphone(IObserver):
    def __init__(self, nome, observable):
        self.nome = nome
        self.observable = observable

    def update(self) -> None:
        observable_name = self.osbervable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} foi atualizado'
              '=> {self.observable.state}')


if __name__ == "__main__":
    weather_station = WeatherStation()

    smartphone = Smartphone('iphone', weather_station)

    weather_station.add_observer(smartphone)

    weather_station.state = {'Temperatura': 30}
