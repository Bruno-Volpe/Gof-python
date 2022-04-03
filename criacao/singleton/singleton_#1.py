"""
Singeton garante que uma classe tenha somanete uma instacia e fornece um ponto
global de acesso para a mesma!
Exs: Base de dados, configs ( COISAS UNICAS )
"""


class AppSettings:

    # De forma geral, isso ja eh um singletom
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    # Fim do singleton MUITO basico

    def __init__(self):
        self.tema = 'Dark'
        self.font = '18px'


if __name__ == "__main__":
    as1 = AppSettings()
    as2 = AppSettings()
