""" 1. Programación Modular-Estructura """
def promedio(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma / len(numeros)
def desviacion(numeros):
    prom = promedio(numeros)
    suma = 0
    for numero in numeros:
        suma += (numero - prom) ** 2
    return (suma / (len(numeros) - 1))**0.5

numeros = []
print("Ingrese 10 números:")
for i in range(10):
    numero = float(input("Número " + str(i + 1) + ": "))
    numeros.append(numero)
print("El promedio es %.2f" % promedio(numeros))
print("La desviación estándar es %.5f" % desviacion(numeros))
""" 2. Programación Orientada a Objetos """
class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros
    def promedio(self):
        suma = 0
        for numero in self.numeros:
            suma += numero
        return suma / len(self.numeros)
    def desviacion(self):
        prom = self.promedio()
        suma = 0
        for numero in self.numeros:
            suma += (numero - prom) ** 2
        return (suma / (len(self.numeros) - 1))**0.5

numeros = []
print("Ingrese 10 números:")
for i in range(10):
    numero = float(input("Número " + str(i + 1) + ": "))
    numeros.append(numero)
estadistica = Estadistica(numeros)
print("El promedio es %.2f" % estadistica.promedio())
print("La desviación estándar es %.5f" % estadistica.desviacion())
