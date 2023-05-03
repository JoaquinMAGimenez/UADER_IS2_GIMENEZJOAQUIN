#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#*--------------------------------------------------

# Componente abstracto
class Numero():
    def imprimir(self):
        pass

# Implementación concreta del componente
class NumeroConcreto(Numero):
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print(f"Valor actual: {self.valor}")
# Decorador abstracto
class Operacion(Numero):
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        self.numero.imprimir()

# Decorador concreto que suma 2
class SumaDos(Operacion):
    def __init__(self, numero):
        super().__init__(numero)
        self.valor= self.numero.valor

    def imprimir(self):
        super().imprimir()

        self.numero.valor = self.valor + 2
        print(f"Valor sumado 2: {self.numero.valor}")

# Decorador concreto que multiplica por 2
class MultiplicarPorDos(Operacion):
    def __init__(self, numero):
        super().__init__(numero)
        self.valor=self.numero.valor

    def imprimir(self):
        super().imprimir()
        self.numero.valor =self.valor * 2
        print(f"Valor multiplicado por 2: {self.numero.valor}")

# Decorador concreto que divide por 3
class DividirPorTres(Operacion):
    def __init__(self, numero):
        super().__init__(numero)
        self.valor=self.numero.valor

    def imprimir(self):
        super().imprimir()
        self.numero.valor = self.valor / 3
        print(f"Valor dividido por 3: {self.numero.valor}")
        
# Ejemplo de uso-
numero = NumeroConcreto(7)

# Imprimir valor actual sin decoradores
numero.imprimir()

# Decorador suma 2
numero = SumaDos(numero)
numero.imprimir()

# Decorador multiplicar por 2
numero = MultiplicarPorDos(numero)
numero.imprimir()

# Decorador dividir por 3
numero = DividirPorTres(numero)
numero.imprimir() 