"""
Builder: Tem a itencao de separa a construao de um objeto complexo, de modo que
o mesmo processo de cosnrucao possa criar diferentes representacoes.

Nao eh muito interessante pra python
"""
from abc import ABC, abstractmethod


class User:
    def __init__(self):  # Poderiamos passar os parametros, dessa forma nao eh nescessario o uso do builder
        self.firstname = None
        self.lastname = None
        self.age = None


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self): pass

    @abstractmethod
    def add_firsname(self, firstname): pass

    @abstractmethod
    def add_lasname(self, lastname): pass

    @abstractmethod
    def add_age(self, age): pass


class UserBuilder(ABC):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_firsname(self, firstname):
        self.result.firstname = firstname

    def add_lasname(self, lastname):
        self.result.lastname = lastname

    def add_age(self, age):
        self.result.age = age


class UserDirector:
    def __init__(self, builder):
        self._builder = builder

    def with_age(self, first_name, last_name, age):
        self._builder.add_firstname()
        self._builder.add_lastname()
        self._builder.add_age()

        return self._builder.result


if __name__ == "__main__":
    user_builder = Userbuilder()
    user_director = UserDirector(user_builder)
