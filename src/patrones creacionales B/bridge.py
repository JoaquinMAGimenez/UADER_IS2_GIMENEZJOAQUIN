#*--------------------------------------------------
#* bridge.py
#* excerpt from https://refactoring.guru/design-patterns/bridge/python/example
#*--------------------------------------------------

# Implementación de los trenes laminadores
class TrenLaminador:
    def producir_lamina(self):
        pass

class TrenLaminador5Mts(TrenLaminador):
    def producir_lamina(self):
        print("Produciendo lámina de 5 metros")

class TrenLaminador10Mts(TrenLaminador):
    def producir_lamina(self):
        print("Produciendo lámina de 10 metros")

# Abstracción de las láminas
class Lamina:
    def __init__(self, tren_laminador, espesor, ancho):
        self.tren_laminador = tren_laminador
        self.espesor = espesor
        self.ancho = ancho

    def producir(self):
        self.tren_laminador.producir_lamina()

tren_5mts = TrenLaminador5Mts()
tren_10mts = TrenLaminador10Mts()

lamina_5mts = Lamina(tren_5mts, 0.5, 1.5)
lamina_10mts = Lamina(tren_10mts, 0.5, 1.5)

lamina_5mts.producir() # Producción de lámina de 5 metros de longitud
lamina_10mts.producir() # Producción de lámina de 10 metros de longitud

