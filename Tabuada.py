class Tabuada:
    def __init__(self, numero, vezes):
        self.numero = numero
        self.vezes = vezes

    def exibir_Tabuada(self):
        print(f"---- TABUADA DO {self.numero} ATÉ {self.vezes} ----")

        for i in range(1, self.vezes + 1):
            print(f"{self.numero} x {i} = {self.numero*i}")



numero = int(input("Qual tabuada você quer: "))
vezes = int(input("Até qual: "))

tabuada = Tabuada(numero, vezes)
tabuada.exibir_Tabuada()
