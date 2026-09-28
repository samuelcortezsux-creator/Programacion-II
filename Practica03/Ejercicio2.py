import random
class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.numeroDeVidas = 3
    def actualizaRecord(self):
        self.record = self.record + 1
    def quitaVida(self):
        self.numeroDeVidas = self.numeroDeVidas - 1

        if self.numeroDeVidas > 0:
            return True
        else:
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = 0
    def validaNumero(self, numero):
        if numero >= 0 and numero <= 10:
            return True
        else:
            return False
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Adivina un número entre 0 y 10")
        while True:
            numero = int(input("Ingrese un número: "))
            if not self.validaNumero(numero):
                print("Número inválido. Debe estar entre 0 y 10")
                continue
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break
            else:
                quedanVidas = self.quitaVida()
                if quedanVidas:
                    if numero < self.numeroAAdivinar:
                        print("El número a adivinar es MAYOR")
                    else:
                        print("El número a adivinar es MENOR")
                    print("Vidas restantes:", self.numeroDeVidas)
                else:
                    print("Te quedaste sin vidas")
                    print("El número era:", self.numeroAAdivinar)
                    break
    def validaNumero(self, numero):
        return 0 <= numero <= 10
    def juega(self):
        self.reiniciaPartida()
        self.numeroAAdivinar = random.randint(0, 10)
        while True:
            numero = int(input("Adivina un número entre 0 y 10: "))
            if not self.validaNumero(numero):
                continue
            if numero == self.numeroAAdivinar:
                print("¡Acertaste!!")
                self.actualizaRecord()
                return
            else:
                if self.quitaVida():
                    if numero < self.numeroAAdivinar:
                        print("El número a adivinar es mayor. Intenta de nuevo.")
                    else:
                        print("El número a adivinar es menor. Intenta de nuevo.")
                else:
                    print("Te quedaste sin vidas. Fin del juego.")
                    return

class JuegoAdivinaImpar(JuegoAdivinaNumero):

    def validaNumero(self, numero):
        if numero < 0 or numero > 10:
            print("Error: debe ingresar un número entre 0 y 10.")
            return False

        if numero % 2 != 0:
            return True
        else:
            print("Error: debe ingresar un número IMPAR.")
            return False

    def juega(self):
        self.reiniciaPartida()

        # Generar solamente números impares
        numerosImpares = [1, 3, 5, 7, 9]
        self.numeroAAdivinar = random.choice(numerosImpares)

        print("\n===== JUEGO IMPAR =====")
        print("Adivina un número IMPAR entre 0 y 10.")

        while True:
            numero = int(input("Adivina un número entre 0 y 10: "))

            if not self.validaNumero(numero):
                continue

            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break

            quedanVidas = self.quitaVida()

            if quedanVidas:
                if numero < self.numeroAAdivinar:
                    print("El número a adivinar es mayor. Intenta de nuevo.")
                else:
                    print("El número a adivinar es menor. Intenta de nuevo.")

                print("Vidas restantes:", self.numeroDeVidas)

            else:
                print("Te quedaste sin vidas.")
                print("El número era:", self.numeroAAdivinar)
                break

class JuegoAdivinaPar(JuegoAdivinaNumero):

    def validaNumero(self, numero):
        if numero < 0 or numero > 10:
            print("Error: debe ingresar un número entre 0 y 10.")
            return False

        if numero % 2 == 0:
            return True
        else:
            print("Error: debe ingresar un número PAR.")
            return False

    def juega(self):
        self.reiniciaPartida()

        # Generar solamente números pares
        numerosPares = [0, 2, 4, 6, 8, 10]
        self.numeroAAdivinar = random.choice(numerosPares)

        print("\n===== JUEGO PAR =====")
        print("Adivina un número PAR entre 0 y 10.")

        while True:
            numero = int(input("Adivina un número entre 0 y 10: "))

            if not self.validaNumero(numero):
                continue

            if numero == self.numeroAAdivinar:
                print("¡Acertaste!")
                self.actualizaRecord()
                break

            quedanVidas = self.quitaVida()

            if quedanVidas:
                if numero < self.numeroAAdivinar:
                    print("El número a adivinar es mayor. Intenta de nuevo.")
                else:
                    print("El número a adivinar es menor. Intenta de nuevo.")

                print("Vidas restantes:", self.numeroDeVidas)

            else:
                print("Te quedaste sin vidas.")
                print("El número era:", self.numeroAAdivinar)
                break

class Aplicacion:
    @staticmethod
    def main():
        juego1 = JuegoAdivinaNumero(3)
        juego2 = JuegoAdivinaPar(3)
        juego3 = JuegoAdivinaImpar(3)
        juego1.juega()
        juego2.juega()
        juego3.juega()
Aplicacion.main()