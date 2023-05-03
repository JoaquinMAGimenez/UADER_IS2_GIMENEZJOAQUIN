#*--------------------------------------------------
#* proxy.py
#* excerpt from https://refactoring.guru/design-patterns/proxy/python/example
#*--------------------------------------------------
#from subprocess import 
from abc import ABC, abstractmethod
from pythonping import ping

# Interface para pingReal y pingProxy
class Subject(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass



class Ping_inicial(Subject):

    def execute(self, ip_direction):
        #Mediante un total de 10 intentos revisa si la IP posee 192 como numeros iniciales
        for i in range(10):
            if self.direction_control(ip_direction):
                # Al cumplirse la condicion en uno de esos 10 intentos se retorna el ping
                return ping(f"{ip_direction}", verbose= True)
    
        # De no ser asi prohibe el acceso con el mensaje "Acceso denegado"
        return ("Acceso denegado")
    

    # Realiza un ping a una direccion sin ningun control
    def execute_free(self, direction):
        print("Realizando ping sin ningun control")
        return ping(f"{direction}", verbose=True)
    
    # Funcion encargada de controlar si una ip comienza con 192
    def direction_control(self, str):
        if(str.startswith("192")):
            return True
        else: return False



class Ping_proxy(Subject):

    def __init__(self, ping_real: Ping_inicial) -> None:
        self.ping_real = ping_real
    def execute(self, ip_direction):
        if(ip_direction == "192.168.0.254"):
            direction = "www.google.com"
            return self.ping_real.execute_free(direction)
        else:
            return self.ping_real.execute(ip_direction)     
        


if __name__ == "__main__":
    ip = "192.168.0.254"

    ping_real = Ping_inicial()

    ping_proxy = Ping_proxy(ping_real)
    print(ping_proxy.execute(ip))