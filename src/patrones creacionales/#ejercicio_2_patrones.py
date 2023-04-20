#ejercicio_2_patrones.py

#https://refactoring.guru/design-patterns/factory-method/python/example

#informacion de ayuda y metodos obtenida de la pagina linkeada anteriormente 

from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    

    @abstractmethod
    def factory_method(self):
        
        pass

    def some_operation(self,num) -> str:
        

       
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.operation(num)}\n"

        return result


class ConcreteCreator1(Creator):
   

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class Product(ABC):
    

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self,num) -> str:
        iva = num * 0.21
        ibb = num * 0.05
        contribuciones_municipales = num * 1.2
        total = iva + ibb + contribuciones_municipales
        return total


def client_code(creator: Creator,num) -> None:
    

    print(f"Yo soy un mero intermediario tipo FACTORY que no se que es lo que estoy creando, pero lo creo.\n"
          f"{creator.some_operation(num)}", end="")


if __name__ == "__main__":
    num=int(input('debe ingresar una base imponible para realizar el calcular: '))
    print("Calculando impuesto 1")
    client_code(ConcreteCreator1(),num)

    num=int(input('debe ingresar una base imponible para realizar el calcular: '))
    print("calculando impuesto 2")
    client_code(ConcreteCreator1(),num)
