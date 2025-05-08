class NumerosPares:
    @staticmethod

    def exibirParesEImpares():
        print("Números Pares e Impares")
        try:
            N = int(input("Digite até que número: "))
            if N < 0:
                print("Digite valores positivos.")
                return
        except ValueError:
            print("Entrada Invalida. Digite um valor numerico.")
            return

        x = 0
        print("Os Pares são:", end=" ")

        while x<=N:
            if(x%2 == 0):
                print(x, end=" ")
            x = x + 1

        print()

        x = 0
        print("Os Impares são:", end=" ")
        while x <= N:
            if x % 2 == 1:
                print(x, end=" ")
            x+=1


NumerosPares.exibirParesEImpares()
