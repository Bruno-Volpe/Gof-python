"""
Command encpsula uma solicitacao como objeto, desta forma permite parametrizar
clientes com diferentes solicitacoes, enfilerar ou fazer registro (log) de 
solicitacoes e suportar opercoes que podem sr desfeitas.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Light:
    """ Receiver - luz inteligente """

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default Color'

    def on(self) -> None:
        print(f'Light {self.name} is now on')

    def off(self) -> None:
        print(f'Light {self.name} is now off')

    def chance_color(self, color: str) -> None:
        self.color = color
        print(f'Light {self.name} is now {self.color}')


class ICommand(ABC):
    """ Interface de comando """

    @abstrctmethod
    def execute(self) -> None: pass

    @abstrctmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    """ comando concreto """

    def __init__(self, light):
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class RemoteControler:
    """ Invoker """

    def __init__(self) -> None:
        self.button: dict = {}

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()

    def button_pressed_again(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()


if __name__ == "__main__":
    bedroom_light = Light('Luz do quarto', 'Quarto')

    bedroom_light_on = LightOnCommand(bedroom_light)

    remote = RemoteControler()
    remote.button_add_command('first_button') = bedroom_light_on

    remote.button_pressed('first_button')
    remote.button_pressed_again('first_button')
