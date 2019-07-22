import op_matematicas

print('Escolha a opção:\n'
      '1 - Soma de dois números.\n'
      '2 - Diferençan entre dois números (maior pelo menor).\n'
      '3 - Produto entre dois números.\n'
      '4 - Divisão entre dois números (o denominador não pode ser zero).')
opcao = input('Opção: ')

if opcao == '1':
    n1 = int(input("Infome o primeiro número: "))
    n2 = int(input("Infome o segundo número: "))
    resultado = op_matematicas.soma(n1, n2)
    print(f"Soma dos dois números é {resultado}")
elif opcao == '2':

elif opcao == '3':

elif opcao == '4':

else:
    print("Opção inválida !!!")
