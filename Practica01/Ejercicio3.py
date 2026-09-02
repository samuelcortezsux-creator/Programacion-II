""" 1. Programación Modular-Estructura """
class EcuacionLineal:
    def __init__(self, a, b, c):
        self.__a=a
        self.__b=b
        self.__c=c
    def getDiscriminante(self):
        return self.__b**2-4*self.__a*self.__c
    def getRaiz1(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b + d**0.5) / (2 * self.__a)
        else:
            return 0
    def getRaiz2(self):
        d = self.getDiscriminante()
        if d >= 0:
            return (-self.__b - d**0.5) / (2 * self.__a)
        else:
            return 0

a, b, c = map(float, input("Ingrese los valores de a, b y c separados por espacios: ").split())
ecuacion = EcuacionLineal(a, b, c)
d = ecuacion.getDiscriminante()
if d > 0:
    print("La ecuación tiene dos raíces")
    print("r1 =", ecuacion.getRaiz1())
    print("r2 =", ecuacion.getRaiz2())
elif d == 0:
    print("La ecuación tiene una raíz", ecuacion.getRaiz1())
else:
    print("La ecuación no tiene raíces reales")
