#ejercicio_4_patrones.py

# https://refactoring.guru/design-patterns/builder/python/example

#informacion de ayuda y metodos obtenida de la pagina linkeada anteriormente 

class Director:
    __builder = None
   
    def setBuilder(self, builder):
      self.__builder = builder
	   
    def getFactura(self,monto):
      factura = factura()
      
      importe = self.__builder.getImporte(monto)
      factura.setImporte(importe)

      responsble = self.__builder.getCondicionImpositiva()
      factura.condicionImpositiva(responsble)
    
      return factura

class Factura:
      def __init__(self):
         self.importe = None
         self.condicion_impositiva = None

      def setImporte(self, importe):
         self.importe = importe

      def condicionImpositiva(self,condicion_impositiva):
        self.condicion_impositiva= condicion_impositiva

      def specification(self):
         importe =self.importe.size
         condicion=self.condicion_impositiva.condicion
         total=importe * condicion
         print(f"Factura: ", total)


class Builder:
	
      def getImporte(self): pass
      def getCondicionImpositiva(self): pass



class Factura_Builder_Iva_Responsable(Builder):
   
   def getImporte(self, monto):
      importe = Importe()
      importe.size = monto
      return importe
   
   def getCondicionImpositiva(self):
      condicion2 = CondicionImpositiva()
      condicion2.condicion = 1.05
      return condicion2

class Factura_Builder_Iva_Excento(Builder):
   
   def getImporte(self, monto):
      importe = Importe()
      importe.size = monto
      return importe
   
   def getCondicionImpositiva(self):
      condicion2 = CondicionImpositiva()
      condicion2.condicion = 1.0
      return condicion2

class Factura_Builder_Iva_No_Inscripto(Builder):
   
   def getImporte(self, monto):
      importe = Importe()
      importe.size = monto
      return importe
   
   def getCondicionImpositiva(self):
      condicion2 = CondicionImpositiva()
      condicion2.condicion = 1
      return condicion2

class Importe:
   size = None

class CondicionImpositiva:
   condicion = None

def main(monto,responsable):
   if responsable == "IVA Responsable":
      factura = Factura_Builder_Iva_Responsable() 
   elif responsable == "IVA No Inscripto":
      factura = Factura_Builder_Iva_No_Inscripto()
   elif responsable == "IVA Exento":
      factura = Factura_Builder_Iva_Excento()
   director = Director()   
   director.setBuilder(factura)
   factura = director.getfactura(monto)
   factura.specification

if __name__ == "__main__":

   total=int(input('ingrese el total de la factura: '))
   responsable=str(input('ingrese el tipo de responsable incripto: '))
   main(total,responsable)