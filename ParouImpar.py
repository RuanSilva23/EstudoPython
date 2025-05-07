class ParouImapr:
    numero = input("Digite um número: ")
    numero = int(numero)

    multiplicacao = numero * 2

    if multiplicacao % 2 == 0:
        print("O número", multiplicacao, "é Par.")

    else:
        print("O número", multiplicacao, "é Impar.")