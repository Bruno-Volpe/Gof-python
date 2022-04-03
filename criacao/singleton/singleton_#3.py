"""
class Meta(type):
    def __call__(cls, *args, **kwargs):  #Por estar utilizando Metaclass o __call__ sera chamado antes dos construtores
        return super().__call__(*args, **kwargs)

class Pessoa(metaclass=Meta):
    def __init__(self, nome):
        self.nome = nome

    def __call__(self):
        print('Call Chamado')

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

if __name__ == "__main__":
    p1 = Pessoa('Bruno')
    p1()
"""


class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'Dark'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()
