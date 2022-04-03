"""
*** Para python nao eh muito utlil

Ele tem a intencao de fornecer um meio de acessar 
sequencialmente, os elementos de um objeto
agregado sem exporr sua representacao subjacente
"""
from clolectinos.abc import Iterator, Iterable
from type import List, Any


class MyIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index = self._index + 1
            return item
        except IndexError:
            raise StopIteration


class MyList(Iterable):
    def __init__(self):
        self._itens: List[Any] = []

    def add(self, value):
        self._itens.append(value)

    def __iter__(self):
        return MyIterator(self._itens)

    def __str__(self):
        return f'{self.__class__.__name__} ({self._itens})'


if __name__ == "__main__":
    mylist = MyList()
    mylist.add('Brunao')

    # Nao posso chamar o mylist direto pois ele dedicou a tarefa de iterar para Myiterator
    print(next(iter(mylist)))
