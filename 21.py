import op_matematicas

print('Escolha a opção:\n'
      '1 - Soma de dois números.\n'
      '2 - Diferençan entre dois números (maior pelo menor).\n'
      '3 - Produto entre dois números.\n'
      '4 - Divisão entre dois números (o denominador não pode ser zero).')
opcao = int(input('Opção: '))

if opcao < 1 or opcao > 4:
    print("Opção inválida !!!")
else:
    n1 = int(input("Infome o primeiro número: "))
    n2 = int(input("Infome o segundo número: "))
    
    if opcao == 1:
        resultado = op_matematicas.soma(n1, n2)
        print(f"Soma dos dois números é {resultado}")
    elif opcao == 2:
        if n1 < n2:
            print("O primeiro número, não pode ser menor que o segundo !!! "
                  "Execute novamente!")
        else:
            resultado = op_matematicas.subtracao(n1, n2)
            print(f"Diferença entre dois números é {resultado}")
    elif opcao == 3:
        resultado = op_matematicas.produto(n1, n2)
        print(f"Produto entre os dois números é {resultado}")
    else:  # elif opcao == 4:
        if n2 == 0:
            print("O denominador (segundo número), não pode ser 0 (zero) !!! "
                  "Execute novamente !")
        else:
            resultado = op_matematicas.divisao(n1, n2)
            print(f"Divisão entre dois números é {resultado}")
print("Fim do programa !!!")
