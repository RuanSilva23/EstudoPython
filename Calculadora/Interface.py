from xmlrpc.client import boolean


class Interface:
    continuar = boolean(True)
    while continuar:
        print("------Menu-------")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Módulo")
        print("0 - Sair")
        opcao = input("Opção escolhida: ")
        opcao = int(opcao)

        if opcao == 0:
            continuar = False
            print("Encerrando.....")
        if (opcao > 5) or (opcao < 0):
            print("Opção Invalida. Tente Novamente")
            continue



        match opcao:
            case 1:
                x = input("Digite o primeiro valor: ")
                x = int(x)

                y = input("Digite o segundo número:")
                y = int(y)

                soma = x + y
                print("Soma:", soma)

            case 2:
                x = input("Digite o primeiro valor: ")
                x = int(x)

                y = input("Digite o segundo número:")
                y = int(y)

                subtracao = x - y
                print("Subtração:",subtracao)

            case 3:
                x = input("Digite o primeiro valor: ")
                x = int(x)

                y = input("Digite o segundo número:")
                y = int(y)

                multiplicacao = x * y
                print("Multiplicação:", multiplicacao)

            case 4:
                x = input("Digite o primeiro valor: ")
                x = int(x)

                y = input("Digite o segundo número:")
                y = int(y)
                if (y <= 0):
                    print("Não se divide por zero.")
                    
                else:
                    divisao = x / y
                    print("Divisão:", divisao)

            case 5:
                x = input("Digite o primeiro valor: ")
                x = int(x)

                y = input("Digite o segundo número:")
                y = int(y)

                modulo = x % y
                print("Módulo entre os dois números:", modulo)



