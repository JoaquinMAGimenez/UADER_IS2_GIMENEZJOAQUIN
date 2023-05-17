#ejercicio_4.py

import os

# Clase State: Clase base para los estados
class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

    def toggle_amfm(self):
        pass

# Clase AmState: Implementa la sintonización de estaciones de AM
class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

# Clase FmState: Implementa la sintonización de estaciones de FM
class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

# Clase Radio: Construye la radio con todas las formas de sintonización
class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

# Clase RadioWithMemories: Extiende la clase Radio para incluir las frecuencias memorizadas
class RadioWithMemories(Radio):
    def __init__(self):
        super().__init__()
        self.memories = ["M1", "M2", "M3", "M4"]

    def scan_memories(self):
        for memory in self.memories:
            print("Recuperando frecuencia de memoria {}...".format(memory))
            if memory.startswith("M"):
                self.state.scan()

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = RadioWithMemories()
    actions = [radio.scan_memories] * 2 + [radio.toggle_amfm] + [radio.scan_memories] * 2
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()