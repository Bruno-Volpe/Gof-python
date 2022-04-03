"""
Eh um padrao comportamental que tem a intencao de evitar
o acoplamento do remetente de uma solicitacao ao seu receptor, ao dar um objeto
a oportunidade de tratar a solicitacao.
"""
from abc import abstractmethod, ABC


class Handler(ABC):
    def __init__(self):
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
     def __init__(self, sucessor: Handler):
         self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{letter} tratada com sucesso'
        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
     def __init__(self, sucessor: Handler):
         self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'{letter} tratada com sucesso'
        return self.sucessor.handle(letter)
    
class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'{letter} nao foi tratada com sucesso'


if __name__ == "__main__":
    handler_unsloved = HundlerUnsolverd()
    hamdler_def = HandlerDEF(handler_unsolved)
    handler_abc = HandlerABC(handler_def)
