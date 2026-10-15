import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.vidasIniciales = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = self.vidasIniciales
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    def quitaVida(self):
        self.numeroDeVidas -= 1
        return self.numeroDeVidas > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    def generaNumero(self):
        return random.randint(0, 10)
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = self.generaNumero()
        print("Adivina un número entre 0 y 10:")
        while self.numeroDeVidas > 0:
            numero = int(input())
            if not self.validaNumero(numero):
                continue
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                return
            if self.quitaVida():
                if self.numeroAAdivinar > numero:
                    print("El número a adivinar es MAYOR")
                else:
                    print("El número a adivinar es MENOR")
            else:
                print(f"Sin vidas. El número era {self.numeroAAdivinar}")
                return
class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero % 2 != 0:
            print("Error: debes ingresar un número PAR.")
            return False
        return super().validaNumero(numero)
    def generaNumero(self):
        return random.choice([0, 2, 4, 6, 8, 10])
class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if numero % 2 == 0:
            print("Error: debes ingresar un número IMPAR.")
            return False
        return super().validaNumero(numero)
    def generaNumero(self):
        return random.choice([1, 3, 5, 7, 9])
class Aplicacion:
    @staticmethod
    def main():
        juegos = [
            ("Juego normal", JuegoAdivinaNumero(3)),
            ("Juego de pares", JuegoAdivinaPar(3)),
            ("Juego de impares", JuegoAdivinaImpar(3)),
        ]
        for nombre, juego in juegos:
            print(f"=== {nombre} ===")
            juego.juega()    
Aplicacion.main()