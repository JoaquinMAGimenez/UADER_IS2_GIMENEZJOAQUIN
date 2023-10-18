# Calculando el número de iteraciones del algoritmo de Collatz
def collatz(num):
    if not isinstance(num, int) or num <= 0:
        print("Error: Entrada no válida. Ingrese un número entero positivo.")
        return -1  # Devuelve un valor especial para indicar un error
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

# Comprobando los resultados
i = 25  # Número negativo o letras para probar el mensaje de error
if not isinstance(i, int) or i <= 0:
    print("Error: Entrada no válida. Ingrese un número entero positivo.")
else:
    print("El número de iteraciones para %d es %d\n" % (i, collatz(i)))
