import matplotlib.pyplot as plt
import numpy as np

# X axis parameter:
#xaxis = np.array([2, 8])

# Y axis parameter:
#yaxis = np.array([4, 9])

#plt.plot(xaxis, yaxis)
#plt.show()

#n = int(input('ingrese un numero mayor a 0'));
#if n > 0:
    #while n != 1:
   #     if n % 2 == 0:
    #        n = n / 2
 #       else:
  #          n = n*3+1;
#else:
 #   print ('debe ingresar un numero mayor a 0');

#print(n)

def collatz(n):
    susecion = [n];
    if n==1:
        susecion.append(n);
        return susecion;
    if n > 0:
        while n != 1:
         if n % 2:
            n = n*3+1
         else:
            n = n // 2;
            susecion.append(n);
    
    return susecion;


arrayejeX =[];

arrayejeY = [];

for h in range (1,10000):
   resultado_final = collatz(h);
   arrayejeX.append(h);

   arrayejeY.append(len(resultado_final));

plt.plot(arrayejeX, arrayejeY);

plt.show()

#tuve problemas con la libreria numpy y la solucion fue no colocar la carpeta del codigo en el explorador del visual estudio code 
# y realizar el ejercicio sobre el archivo de lineas por eso aparece copiado sobre este mismo