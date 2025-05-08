class NumerosPares:
    @staticmethod

    def exibirPares():
        print("Números Pares")
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

NumerosPares.exibirPares()