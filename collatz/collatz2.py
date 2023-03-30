import matplotlib.pyplot as plt
import numpy as np

# X axis parameter:
#xaxis = np.array([2, 8])

# Y axis parameter:
#yaxis = np.array([4, 9])

#plt.plot(xaxis, yaxis)
#plt.show()

n = int(input('ingrese un numero mayor a 0'));
if n > 0:
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3+1;
else:
    print ('debe ingresar un numero mayor a 0');

print(n)

def collatz(n):
    susecion = [n]
    if n==1:
        susecion.append(n)
        return susecion
    if n > 0:
        while n != 1:
         if n % 2:
            n = n*3+1
         else:
            n //  2;
    


arrayejeX = np.array([])

arrayejeY = np.array([])

plt.plot(arrayejeX, arrayejeY)
plt.show()