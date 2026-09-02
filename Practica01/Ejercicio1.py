import time
import random
class Cronometro:
    def __init__(self):
        self.inicia = time.time()
        self.finaliza = 0
    def getinicia(self):
        return self.inicia
    def getfinaliza(self):
        return self.finaliza
    def inicia(self):
        self.inicia = time.time()
    def detener(self):
        self.finaliza = time.time()
    def lapsoDeTiempo(self):
        return (self.__finaliza - self.__inicia) * 1000
def ordenacionSeleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[minimo]:
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]

numeros = []
for i in range(100000):
    numeros.append(random.randint(0, 1000000))
cronometro = Cronometro()
cronometro.inicia()
ordenacionSeleccion(numeros)
cronometro.detener()
print("Cantidad de números:", len(numeros))
print("Tiempo de ejecución:", cronometro.lapsoDeTiempo(), "milisegundos")