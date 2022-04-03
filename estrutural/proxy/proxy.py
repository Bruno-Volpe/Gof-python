"""
O Proxy é um padrão de projeto estrutural que tem a
intenção de fornecer um objeto substituto que atua
como se fosse o objeto real que o código cliente
gostaria de usar.

O proxy receberá as solicitações e terá controle
sobre como e quando repassar tais solicitações ao
objeto real.

Com base no modo como o proxies são usados,
nós os classificamos como:
- Proxy Virtual: controla acesso a recursos que podem
ser caros para criação ou utilização.

- Proxy Remoto: controla acesso a recursos que estão
em servidores remotos.

- Proxy de proteção: controla acesso a recursos que
possam necessitar autenticação ou permissão.

- Proxy inteligente: além de controlar acesso ao
objeto real, também executa tarefas adicionais para
saber quando e como executar determinadas ações.

Proxies podem fazer várias coisas diferentes:
criar logs, autenticar usuários, distribuir serviços,
criar cache, criar e destruir objetos, adiar execuções
e muito mais...
"""
from abc import ABC, abstractmethod
from time import sleep

class IUser(ABC):
    firsname: str
    lasname: str

    @abstractmethod
    def get_adresses(self) -> list: pass

    @abstractmethod
    def get_all_user_data(self) -> dict: pass


class RealUser(IUser):
    def __init__(self, firstname, lastname):
        sleep(2)  #Simulando requisicao
        self.firstname = firstname
        self.lastname = lastname

    def get_adresses(self) -> list:
        sleep(2)  #Simulando requisicao
        return [
            {'rua': '123 de goiabada'}
        ]

    def get_all_user_data(self) -> dict: 
        sleep(2)  #Simulando requisicao
        return {'cpf': '123123123'}

    
class UserProxy(IUser):
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self._real_user: RealUser

        # Esse objetos ainda nao existem nesse ponto do codigo
        self.cached_adresses: list
        self.all_user_data: dict
    
    def get_real_user(self):
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)
    
    def get_adresses(self) -> list:
        self.get_real_user()

        if not hasattr(self, 'cached_adresses'):
            self.cached_adresses = self._real_user.get_adresses()

        return self._cached_adresses

    def get_all_user_data(self) -> dict:
        self.get_real_user()

        if not hasattr(self, 'all_user_data'):
            self.all_user_data = self._real_user.all_user_data()

        return self.all_user_data