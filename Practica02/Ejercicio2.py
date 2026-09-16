import math
class Vector:
    def __init__(self, *componentes):
        if len(componentes) == 2:
            x, y = componentes
            self.__comp = (x, y, 0)  
            self.__dimension = 2
        elif len(componentes) == 3:
            self.__comp = tuple(componentes)
            self.__dimension = 3
        else:
            raise ValueError("Un Vector se crea con 2 componentes (x, y) o 3 (x, y, z).")
    def get_x(self):
        return self.__comp[0]
    def get_y(self):
        return self.__comp[1]
    def get_z(self):
        return self.__comp[2]
    def get_dimension(self):
        return self.__dimension
    def suma(self, otro):
        return Vector(self.get_x() + otro.get_x(),
                        self.get_y() + otro.get_y(),
                        self.get_z() + otro.get_z())
    def resta(self, otro):
        return Vector(self.get_x() - otro.get_x(),
                        self.get_y() - otro.get_y(),
                        self.get_z() - otro.get_z())
    def escala(self, r):
        return Vector(self.get_x() * r, self.get_y() * r, self.get_z() * r)
    def punto(self, otro):
        return (self.get_x() * otro.get_x() +
                self.get_y() * otro.get_y() +
                self.get_z() * otro.get_z())
    def cruz(self, otro):
        cx = self.get_y() * otro.get_z() - self.get_z() * otro.get_y()
        cy = self.get_z() * otro.get_x() - self.get_x() * otro.get_z()
        cz = self.get_x() * otro.get_y() - self.get_y() * otro.get_x()
        return Vector(cx, cy, cz)
    def magnitud(self):
        return math.sqrt(self.get_x() ** 2 + self.get_y() ** 2 + self.get_z() ** 2)
    def __str__(self):
        if self.__dimension == 2:
            return f"({self.get_x()}, {self.get_y()})"
        return f"({self.get_x()}, {self.get_y()}, {self.get_z()})"
class AlgebraVectorial:
    TOL = 1e-9
    def __init__(self, a: Vector, b: Vector):
        self.a = a
        self.b = b
    def es_perpendicular(self, metodo=1):
        a, b = self.a, self.b
        if metodo == 1:
            # a) |a + b| = |a - b|
            return math.isclose(a.suma(b).magnitud(), a.resta(b).magnitud(), abs_tol=self.TOL)
        elif metodo == 2:
            return math.isclose(a.resta(b).magnitud(), b.resta(a).magnitud(), abs_tol=self.TOL) 
        elif metodo == 3:
            # c) a · b = 0
            return math.isclose(a.punto(b), 0, abs_tol=self.TOL)
        elif metodo == 4:
            return math.isclose(a.suma(b).magnitud() ** 2,
                                 a.magnitud() ** 2 + b.magnitud() ** 2, abs_tol=self.TOL)
        else:
            raise ValueError("metodo debe ser 1, 2, 3 o 4.")
    def es_paralela(self, metodo=1):
        a, b = self.a, self.b
        if metodo == 1:
            if math.isclose(b.get_x(), 0, abs_tol=self.TOL) or \
                math.isclose(b.get_y(), 0, abs_tol=self.TOL) or \
                math.isclose(b.get_z(), 0, abs_tol=self.TOL):
                return self.es_paralela(metodo=2)
            r_x = a.get_x() / b.get_x()
            r_y = a.get_y() / b.get_y()
            r_z = a.get_z() / b.get_z()
            return math.isclose(r_x, r_y, abs_tol=self.TOL) and \
                math.isclose(r_y, r_z, abs_tol=self.TOL)
        elif metodo == 2:
            # f) a x b = 0
            c = a.cruz(b)
            return math.isclose(c.magnitud(), 0, abs_tol=self.TOL)
        else:
            raise ValueError("metodo debe ser 1 o 2.")
    def proyeccion_a_sobre_b(self):
        a, b = self.a, self.b
        factor = a.punto(b) / (b.magnitud() ** 2)
        return b.escala(factor)
    def componente_a_en_b(self):
        a, b = self.a, self.b
        return a.punto(b) / b.magnitud()
if __name__ == "__main__":
    print("=== Caso 1: vectores perpendiculares ===")
    a1 = Vector(1, 0)
    b1 = Vector(0, 1)
    av1 = AlgebraVectorial(a1, b1)
    print(f"a = {a1}, b = {b1}")
    for m in (1, 2, 3, 4):
        print(f"  ¿Perpendiculares? (criterio {m}): {av1.es_perpendicular(metodo=m)}")
    print(f"  ¿Paralelos? (criterio 1): {av1.es_paralela(metodo=1)}")
    print(f"  ¿Paralelos? (criterio 2): {av1.es_paralela(metodo=2)}")
    print("\n=== Caso 2: vectores paralelos ===")
    a2 = Vector(2, 4)
    b2 = Vector(1, 2)
    av2 = AlgebraVectorial(a2, b2)
    print(f"a = {a2}, b = {b2}")
    print(f"  ¿Paralelos? (criterio 1): {av2.es_paralela(metodo=1)}")
    print(f"  ¿Paralelos? (criterio 2): {av2.es_paralela(metodo=2)}")
    print(f"  ¿Perpendiculares? (criterio 3): {av2.es_perpendicular(metodo=3)}")
    print("\n=== Caso 3: proyección y componente ===")
    a3 = Vector(3, 4)
    b3 = Vector(1, 0)
    av3 = AlgebraVectorial(a3, b3)
    print(f"a = {a3}, b = {b3}")
    proy = av3.proyeccion_a_sobre_b()
    comp = av3.componente_a_en_b()
    print(f"  Proyección de a sobre b: {proy}")
    print(f"  Componente de a en b: {comp:.2f}")
    print("\n=== Caso 4: vectores en 3D ===")
    a4 = Vector(1, 2, 3)
    b4 = Vector(4, 5, 6)
    av4 = AlgebraVectorial(a4, b4)
    print(f"a = {a4}, b = {b4}")
    print(f"  a . b = {a4.punto(b4)}")
    print(f"  a x b = {a4.cruz(b4)}")
    print(f"  Proyección de a sobre b: {av4.proyeccion_a_sobre_b()}")
    print(f"  Componente de a en b: {av4.componente_a_en_b():.2f}")