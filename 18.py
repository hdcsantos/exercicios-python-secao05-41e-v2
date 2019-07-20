import op_matematicas

print('Operacoes matematicas')

operacao = input('Qual operacão matemática voce deseja fazer, dentre as principais? ')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if operacao == 'soma':
    # r = op_matematicas.soma(n1, n2)
    print(f'Resultado da soma é {op_matematicas.soma(n1, n2)}')
elif operacao == 'subtracao':
    print(f'Resultado da subtração é {op_matematicas.subtracao(n1, n2)}')
elif operacao == 'multiplicacao':
    print(f'Resultado da multiplicação é {op_matematicas.multiplicacao(n1, n2)}')
elif operacao == 'divisao':
    print(f'Resultado da divisão é {op_matematicas.divisao(n1, n2)}')
elif operacao == 'resto':
    print(f'Resultado da divisão é {op_matematicas.resto(n1, n2)}')    
else:
    print("Operação desconhecida !!!")
