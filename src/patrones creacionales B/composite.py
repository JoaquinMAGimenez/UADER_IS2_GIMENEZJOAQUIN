from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


# Componente base
class Componente:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("-" * nivel + self.nombre)


# Hoja
class Pieza(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)


# Composite
class Conjunto(Componente):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.componentes = []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def remover_componente(self, componente):
        self.componentes.remove(componente)

    def mostrar(self, nivel=0):
        print("-" * nivel + self.nombre)
        for componente in self.componentes:
            componente.mostrar(nivel + 1)


# Ejemplo de uso
producto_principal = Conjunto("Producto principal")

conjunto_1 = Conjunto("Subconjunto 1")
conjunto_2 = Conjunto("Subconjunto 2")
conjunto_3 = Conjunto("Subconjunto 3")

for i in range(4):
    pieza_1 = Pieza(f"Pieza {i+1}")
    pieza_2 = Pieza(f"Pieza {i+1}")
    pieza_3 = Pieza(f"Pieza {i+1}")

    conjunto_1.agregar_componente(pieza_1)
    conjunto_2.agregar_componente(pieza_2)
    conjunto_3.agregar_componente(pieza_3)

producto_principal.agregar_componente(conjunto_1)
producto_principal.agregar_componente(conjunto_2)
producto_principal.agregar_componente(conjunto_3)

producto_opcional = Conjunto("Producto opcional")
for i in range(4):
    pieza_opcional = Pieza(f"Pieza opcional {i+1}")
    producto_opcional.agregar_componente(pieza_opcional)

producto_principal.agregar_componente(producto_opcional)

producto_principal.mostrar()
