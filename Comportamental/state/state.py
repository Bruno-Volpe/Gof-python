"""
State tem a intencao de permititir a um objeto mudar seu comportamento quando 
seu estado interno mudar
"""
from abc import ABC, abstractmethods
from __future__ import annotations

class Order:
    """ Context """
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending()
    
    def pending(self):
        self.pendindg() 

    def approve(self):
        self.approve()

    def reject(self):
        self.reject()
    
class OrderState(ABC):
    def __init__(self):
        self.order = order
        
    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass


class PaymentPending(OrderState):
    def __init__(self):
        self.order = order
    
    def pending(self) -> None:
        print('Pagamento ja pendente')

    def approve(self) -> None:
        self.order.state = PaymentApprove()  # Dessa forma eliminamos os if's do nosso codigo 
        print('Pagamento aprovado')

    def reject(self) -> None: pass


class PaymentAprove(OrderState):
    def __init__(self):
        self.order = order
    
    def pending(self) -> None: pass

    def approve(self) -> None: pass

    def reject(self) -> None: pass


class PaymentRejected(OrderState):
    def __init__(self):
        self.order = order
    
    def pending(self) -> None: pass

    def approve(self) -> None: pass

    def reject(self) -> None: pass