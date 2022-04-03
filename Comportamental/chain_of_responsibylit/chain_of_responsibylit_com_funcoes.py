"""
Eh um padrao comportamental que tem a intencao de evitar
o acoplamento do remetente de uma solicitacao ao seu receptor, ao dar um objeto
a oportunidade de tratar a solicitacao.
"""
# Implementando com funcoes


def handler_ABC(letra: str) -> str:
    letters = ['A', 'B', 'C']

    if letter in letters:
        return f'Consegui tratar o valor da {letter}'
    return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
     letters = ['D', 'E', 'F']

    if letter in letters:
        return f'Consegui tratar o valor da {letter}'
    return handler_unsloved(letter)

def  handler_unsloved(letter: str)->str:
    return f'Nao sei tratar a {letter}'
