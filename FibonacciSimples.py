class Fibonacci:
    x = int(input("Quantos termos: "))

    n = 0
    n1 = 1

    i = 1
    print()
    print("Os números são:", end=" ")
    for i in range(x):
        print(n, end=" ")

        soma = n + n1
        n = n1
        n1 = soma

