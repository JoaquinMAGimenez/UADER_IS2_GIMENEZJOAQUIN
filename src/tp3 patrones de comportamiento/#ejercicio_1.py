#ejercicio_1.py

class Handler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, number):
        if self.can_handle(number):
            self.consume(number)
        elif self.successor:
            self.successor.handle(number)
        else:
            print(f"El número {number} no ha sido consumido.")

    def can_handle(self, number):
        raise NotImplementedError()

    def consume(self, number):
        raise NotImplementedError()


class PrimesHandler(Handler):
    def can_handle(self, number):
        return self.is_prime(number)

    def consume(self, number):
        print(f"El número {number} es primo y ha sido consumido.")

    def is_prime(self, number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True


class EvenHandler(Handler):
    def can_handle(self, number):
        return number % 2 == 0

    def consume(self, number):
        print(f"El número {number} es par y ha sido consumido.")


class Chain:
    def __init__(self):
        self.handler_chain = self.build_chain()

    def build_chain(self):
        handler1 = PrimesHandler()
        handler2 = EvenHandler(handler1)
        return handler2

    def process_numbers(self, start, end):
        for number in range(start, end + 1):
            self.handler_chain.handle(number)


# Uso del patrón cadena de responsabilidad
chain = Chain()
chain.process_numbers(1, 100)