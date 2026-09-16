import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def distancia(self, otro=None, x=None, y=None):
        if otro is not None:
            dx = self.__x - otro.get_x()
            dy = self.__y - otro.get_y()
        elif x is not None and y is not None:
            dx = self.__x - x
            dy = self.__y - y
        else:
            raise ValueError("Debes pasar un objeto MiPunto, o los valores x e y.")
        return math.sqrt(dx ** 2 + dy ** 2)
    def __str__(self):
        return f"({self.__x}, {self.__y})"
if __name__ == "__main__":
    p1 = MiPunto()         
    p2 = MiPunto(10, 30.5)  
    print(f"Punto 1: {p1}")
    print(f"Punto 2: {p2}")
    d1 = p1.distancia(p2)
    print(f"Distancia entre p1 y p2 (usando objeto MiPunto): {d1:.2f}")
    d2 = p1.distancia(x=10, y=30.5)
    print(f"Distancia entre p1 y (10, 30.5) (usando x, y): {d2:.2f}")