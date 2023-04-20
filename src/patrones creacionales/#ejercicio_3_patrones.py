#ejercicio_3_patrones.py

# https://refactoring.guru/es/design-patterns/abstract-factory/python/example

#informacion de ayuda y metodos obtenida de la pagina linkeada anteriormente 

from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    
    @abstractmethod
    def factory_method(self):
        pass

    def algunas_operaciones(self) -> str:
        
        
        product = self.factory_method()

        result = product.operation()

        return result


class Creator_Envio_Por_Delivery(Creator):
    
    def factory_method(self) -> Product:
        return Envio_Por_Delivery()


class Creator_Entregado_Por_Mostrador(Creator):
    def factory_method(self) -> Product:
        return Entregado_Por_Mostrador()

class Creator_Retirado_Por_Cliente(Creator):
    def factory_method(self) -> Product:
        return Retirado_Por_Cliente()


class Product(ABC):
   
    @abstractmethod
    def operation(self) -> str:
        pass


class Envio_Por_Delivery(Product):
    def operation(self) -> str:
        return "envio por delivery"


class Entregado_Por_Mostrador(Product):
    def operation(self) -> str:
        return "Entregada por mostrador"


class Retirado_Por_Cliente(Product):
    def operation(self) -> str:
        return "Retirada por el cliente"


def client_code(creator: Creator) -> None:
    print(creator.algunas_operaciones())


if __name__ == "__main__":
    print("Creando una hambuerguesa")
    cliente1 = client_code(Creator_Envio_Por_Delivery())

    print("Creando una hambuerguesa")
    cliente2=client_code(Creator_Entregado_Por_Mostrador())

    print("Creando una hambuerguesa")
    cliente3=client_code(Creator_Retirado_Por_Cliente())