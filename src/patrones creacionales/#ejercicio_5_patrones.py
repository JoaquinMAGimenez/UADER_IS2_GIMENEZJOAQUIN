#ejercicio_5_patrones.py


class Director:
    __builder = None
   
    def setBuilder(self, builder):
      self.__builder = builder
	   
    def getAvion(self):
      avion = Avion()
      
      # Primero el fusilaje
      body = self.__builder.getBody()
      avion.setBody(body)
      
      # Turbinas
      engine = self.__builder.getengine()
      avion.setengine(engine)

      # tren de aterrizaje
      alas = self.__builder.getAla()
      avion.setAlas(alas)

      # tren de aterrizaje
      tren = self.__builder.getTren()
      avion.attachTren(tren)

      # Retorna el avion completo
      return avion


class Avion:
   def __init__(self):
      self.__tren = None
      self.__engine = None
      self.__body = None
      self.__ala = None

   def setBody(self, body):
      self.__body = body

   def attachTren(self, tren):
      self.__tren=tren

   def setengine(self, engine):
      self.__engine = engine

   def setAlas(self, ala):
      self.__ala = ala

   def specification(self):
      print ("fuselaje: %s" % (self.__body.shape))
      print ("Turbina: %d" % (self.__engine.turbina))
      print ("Tren de aterrizaje:%d" % (self.__tren.tren_aterrizaje))
      print ("Cantidad de alas: %d" % (self.__ala.cant_ala))

class Builder:
	
      def getTren(self): pass
      def getengine(self): pass
      def getBody(self): pass
      def getAla(self): pass

class Avion_Builder(Builder):
   
   def getTren(self):
      tren = Tren()
      tren.tren_aterrizaje = 1
      return tren
   
   def getengine(self):
      Engine = engine()
      engine.turbina = 2
      return engine
   
   def getBody(self):
      body = Body()
      body.shape = "el tipo de cuerpo es semi monocasco"
      return body

   def getAla(self):
      ala = Ala()
      ala.cant_ala = 2
      return ala

class Tren:
   tren_aterrizaje = None

class engine:
   turbina = None

class Body:
   shape = None

class Ala:
   cant_ala = None

def main():
   avionBuilder = Avion_Builder() 
   director = Director() 
   director.setBuilder(avionBuilder)
   avion = director.getAvion()
   avion.specification()

if __name__ == "__main__":

   print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion")

   main()