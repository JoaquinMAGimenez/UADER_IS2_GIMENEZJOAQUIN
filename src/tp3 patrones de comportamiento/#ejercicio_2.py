#ejercicio_2.py

class ReverseIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = len(collection)

    def has_next(self):
        return self.index > 0

    def next(self):
        self.index -= 1
        return self.collection[self.index]


class ForwardIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def has_next(self):
        return self.index < len(self.collection)

    def next(self):
        element = self.collection[self.index]
        self.index += 1
        return element


class StringIterator:
    def __init__(self, string):
        self.string = string

    def reverse_iterator(self):
        return ReverseIterator(self.string)

    def forward_iterator(self):
        return ForwardIterator(self.string)


# Uso del patrón Iterator
my_string = "Hola, mundo!"

iterator = StringIterator(my_string)

print("Recorrido directo:")
forward_iter = iterator.forward_iterator()
while forward_iter.has_next():
    print(forward_iter.next())

print("\nRecorrido inverso:")
reverse_iter = iterator.reverse_iterator()
while reverse_iter.has_next():
    print(reverse_iter.next())