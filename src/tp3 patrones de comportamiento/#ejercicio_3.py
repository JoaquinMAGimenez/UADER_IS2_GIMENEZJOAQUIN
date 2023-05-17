#ejercicio_3.py

class Observer:
    def __init__(self, observer_id):
        self.observer_id = observer_id

    def update(self, emitted_id):
        if emitted_id == self.observer_id:
            print(f"ID coincidente detectado por {self.__class__.__name__}: {emitted_id}")


class ClassA(Observer):
    def __init__(self):
        super().__init__("ID01")


class ClassB(Observer):
    def __init__(self):
        super().__init__("ID02")


class ClassC(Observer):
    def __init__(self):
        super().__init__("ID03")


class ClassD(Observer):
    def __init__(self):
        super().__init__("ID04")


class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def emit_id(self, emitted_id):
        for observer in self.observers:
            observer.update(emitted_id)


# Uso del patrón Observer
subject = Subject()

class_a = ClassA()
class_b = ClassB()
class_c = ClassC()
class_d = ClassD()

subject.add_observer(class_a)
subject.add_observer(class_b)
subject.add_observer(class_c)
subject.add_observer(class_d)

# Emitir 8 IDs, al menos 4 de ellos coincidirán con los IDs de las clases implementadas
ids = ["ID01", "ID05", "ID02", "ID03", "ID06", "ID07", "ID08", "ID04"]
for emitted_id in ids:
    subject.emit_id(emitted_id)