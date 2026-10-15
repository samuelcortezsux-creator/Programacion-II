import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidasIniciales = numeroDeVidas
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = self.numeroDeVidasIniciales
    def actualizaRecord(self):
        if self.numeroDeVidas > self.record:
            self.record = self.numeroDeVidas
    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1
        return self.numeroDeVidas > 0
class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")
        while self.numeroDeVidas > 0:
            numero = int(input())
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                return
            else:
                quedanVidas = self.quitaVida()
                if quedanVidas:
                    if numero < self.numeroAAdivinar:
                        print("El número a adivinar es MAYOR")
                    else:
                        print("El número a adivinar es MENOR")
                else:
                    print(f"Sin vidas. El número era {self.numeroAAdivinar}")
                    return
class Aplicacion:
    @staticmethod
    def main():
        juego = JuegoAdivinaNumero(3)
        juego.juega()
Aplicacion.main()