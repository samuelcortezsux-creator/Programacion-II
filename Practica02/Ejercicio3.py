import math
class Vector3D:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
    def __add__(self, otro):
        return Vector3D(self.a1 + otro.a1,
                            self.a2 + otro.a2,
                            self.a3 + otro.a3)
    def __sub__(self, otro):
        return Vector3D(self.a1 - otro.a1,
                            self.a2 - otro.a2,
                            self.a3 - otro.a3)
    def __mul__(self, r):
        return Vector3D(r * self.a1, r * self.a2, r * self.a3)
    def __rmul__(self, r):
        return self.__mul__(r)
    def __abs__(self):
        return math.sqrt(self.a1 ** 2 + self.a2 ** 2 + self.a3 ** 2)
    def normal(self):
        mag = abs(self)
        return Vector3D(self.a1 / mag, self.a2 / mag, self.a3 / mag)
    def __matmul__(self, otro):
        return self.a1 * otro.a1 + self.a2 * otro.a2 + self.a3 * otro.a3
    def __xor__(self, otro):
        return Vector3D(
            self.a2 * otro.a3 - self.a3 * otro.a2,
            self.a3 * otro.a1 - self.a1 * otro.a3,
            self.a1 * otro.a2 - self.a2 * otro.a1,
        )
    def __eq__(self, otro):
        tol = 1e-9
        return (math.isclose(self.a1, otro.a1, abs_tol=tol) and
                math.isclose(self.a2, otro.a2, abs_tol=tol) and
                math.isclose(self.a3, otro.a3, abs_tol=tol))
    def __str__(self):
        return f"({self.a1}, {self.a2}, {self.a3})"
class AlgebraVectorial:
    TOL = 1e-9
    def __init__(self, a: Vector3D, b: Vector3D):
        self.a = a
        self.b = b
    def es_perpendicular(self, metodo=1):
        a, b = self.a, self.b
        if metodo == 1:   
            return math.isclose(abs(a + b), abs(a - b), abs_tol=self.TOL)
        elif metodo == 2:   
            return math.isclose(abs(a - b), abs(b - a), abs_tol=self.TOL)
        elif metodo == 3:    
            return math.isclose(a @ b, 0, abs_tol=self.TOL)
        elif metodo == 4:    
            return math.isclose(abs(a + b) ** 2, abs(a) ** 2 + abs(b) ** 2,
                                    abs_tol=self.TOL)
        raise ValueError("metodo debe ser 1, 2, 3 o 4.")
    def es_paralela(self, metodo=1):
        a, b = self.a, self.b
        if metodo == 1:       
            return abs(a ^ b) < self.TOL  
        elif metodo == 2:     
            return math.isclose(abs(a ^ b), 0, abs_tol=self.TOL)
        raise ValueError("metodo debe ser 1 o 2.")
    def proyeccion_a_sobre_b(self):
        a, b = self.a, self.b
        factor = (a @ b) / (abs(b) ** 2)
        return factor * b
    def componente_a_en_b(self):
        a, b = self.a, self.b
        return (a @ b) / abs(b)
if __name__ == "__main__":
    a = Vector3D(1, 2, 3)
    b = Vector3D(4, 5, 6)
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"\na) Suma a + b            = {a + b}")
    print(f"b) Escalar 2 * a         = {2 * a}   |  a * 3 = {a * 3}")
    print(f"c) Longitud |a|          = {abs(a):.4f}")
    print(f"d) Normal de a           = {a.normal()}")
    print(f"e) Producto escalar a@b  = {a @ b}")
    print(f"f) Producto vectorial a^b = {a ^ b}")
    print("\n--- AlgebraVectorial ---")
    av = AlgebraVectorial(a, b)
    print(f"¿a y b perpendiculares? {av.es_perpendicular(metodo=3)}")
    print(f"¿a y b paralelos?       {av.es_paralela(metodo=2)}")
    print(f"Proyección de a sobre b: {av.proyeccion_a_sobre_b()}")
    print(f"Componente de a en b:    {av.componente_a_en_b():.4f}")
    print("\n--- Caso perpendicular puro ---")
    p1 = Vector3D(1, 0, 0)
    p2 = Vector3D(0, 1, 0)
    av2 = AlgebraVectorial(p1, p2)
    print(f"p1 = {p1}, p2 = {p2}")
    for m in (1, 2, 3, 4):
        print(f"  ¿Perpendiculares? (criterio {m}): {av2.es_perpendicular(metodo=m)}")
    print("\n--- Caso paralelo puro ---")
    q1 = Vector3D(2, 4, 6)
    q2 = Vector3D(1, 2, 3)
    av3 = AlgebraVectorial(q1, q2)
    print(f"q1 = {q1}, q2 = {q2}")
    for m in (1, 2):
        print(f"  ¿Paralelos? (criterio {m}): {av3.es_paralela(metodo=m)}")