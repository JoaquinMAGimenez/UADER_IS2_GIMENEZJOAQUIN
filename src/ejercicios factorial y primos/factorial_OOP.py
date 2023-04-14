class Factorial:
    
    def __init__(self, min, max):
        self.min = int(min) 
        self.max = int(max)

    def run(self):
        for j in range(self.min, self.max +1):
            if(j < 0):
                print(j, ": Un numero negativo es imposible factorearlo por favor no vuelva a cometer este error")
            elif (j==0):
                print(j, ": 1")
            else:
                fact = 1
                n = j
                while(n > 1):
                    fact *= n
                    n -= 1
                print("El Factorial de ", j, "es:", fact)

nuevo_Factorial = Factorial(-10, 10)

nuevo_Factorial.run()