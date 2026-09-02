class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__e=e
        self.__f=f
    def tieneSolucion(self):
        if self.__a*self.__d-self.__b*self.__c==0:
            return False
        else:
            return True
    def getX(self):
        if self.tieneSolucion():
            return (self.__e*self.__d-self.__b*self.__f)/(self.__a*self.__d-self.__b*self.__c)
        else:
            return None
    def getY(self):
        if self.tieneSolucion():
            return (self.__a*self.__f-self.__e*self.__c)/(self.__a*self.__d-self.__b*self.__c)
        else:
            return None

a, b, c, d, e, f = map(float, input("Ingrese los valores de a, b, c, d, e y f separados por espacios: ").split())
ecuacion = EcuacionLineal(a, b, c, d, e, f)
if ecuacion.tieneSolucion():
    print("x =", ecuacion.getX())
    print("y =", ecuacion.getY())
else:
    print("La ecuación no tiene solución")
