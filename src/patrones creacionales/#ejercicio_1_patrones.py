#ejercicio_1_patrones.py

#https://refactoring.guru/design-patterns/singleton/python/example

#informacion de ayuda y metodos obtenida de la pagina linkeada anteriormente 


class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def getfactorial(self, num): 
        if num < 0: 
            print("No debio ingresar un numero negativo ya que su factorial no existe.")

        elif num == 0: 
            return 1
            
        else: 
            fact = 1
            while(num >= 1): 
                fact *= num 
                num -= 1
            return(fact)



if __name__ == "__main__":
    # The client code.
    num=int(input('ingrese un numero para calcular el factorial: '))
    Sing1 = Singleton()
    Sing2 = Singleton()

    if id(Sing1) == id(Sing2):
        print("Singleton esta funcionando, debido a que ingreso las mismas instancias.")
        print("\n")
        print("Factorial de ", num, "es ", Sing1.getfactorial(num))
    else:
        print("Singleton fallo, las instancias ingresadas no son diferentes.")