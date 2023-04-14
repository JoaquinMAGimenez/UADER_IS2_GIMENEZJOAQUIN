#factorial_modificado.py
#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print(num, "! Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 



if len (sys.argv) == 1:
   print("Debe ingresar un numero")
   num1 = int(input("Ingre el numero limite a factorear: "))

   for j in range(1, num1+1):
        if(j < 0):
            print(factorial(j))
        else:
            print("Factorial ",j," es: ", factorial(j)) 

   sys.exit()

elif len (sys.argv) == 2:
    num1 = int(sys.argv[1])
    for j in range(1, num1+1):
        if(j < 0):
            print(factorial(j))
        else:
            print("Factorial ",j," es: ", factorial(j)) 

    sys.exit()


#Archivo modificado, para que solicite al usuario el limite del rango para calcular el factorial 
# desde 0 hacia ese valor.