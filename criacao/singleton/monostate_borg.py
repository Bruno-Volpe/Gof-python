"""
MONOSTATE(borg) - Variacao do singleton que tem a itencao de garantir que o estado
do objeto seja igual para todas as instancinas
"""

""" VARIACAO 1 """


class StringReprMixin:
     def __str__(self):
        params = ','.join([f'{k}={v}' for k, v in self.__dict__.itens()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    _state = {
        'x': 10
        'y': 20
    }

    def __init__(self):
        self.x = None  #Nao ira alterar valor de x, ja que vem antes de cefinir o __dict__
        self.__dict__ = self._state


if __name__ == "__main__":
    m1 = MonoStateSimple()
    m1.x = 25  #Mudara nas 2, pelos principios dos monostate
    m2 = MonoStateSimple()
    
    print(m1)
    print(m2)

""" FIM DA VARIACAO 1 """


""" VARIACAO 2 """
class StringReprMixin:
    def __str__(self):
    params = ','.join([f'{k}={v}' for k, v in self.__dict__.itens()])
    return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonoState(StringReprMixin):
    _state = {
        'x': 10
        'y': 20
    }

    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj.__dict__ = cls._state
        return obj

    def __init__(self):
        self.x = None  #Nao ira alterar valor de x, ja que vem antes de cefinir o __dict__


class A(MonoState):  #Continuara com o mesmo parametros
    pass

if __name__ == "__main__":
    m1 = MonoStateSimple()
    m1.x = 25  #Mudara nas 2, pelos principios dos monostate
    m2 = MonoStateSimple()
    
    print(m1)
    print(m2)
