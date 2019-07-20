print('Numero inteiro divisivel por 3 e 5 mas nao simultaneamente')

numero = int(input('Informe um número, para saber se e ele é divisivel por 3 ou 5: '))

if (numero % 3) == 0 and (numero % 5) == 0:
    print(f'{numero} é divisivel por 5 e 3 simultaneamente')
elif (numero % 3) == 0:
    print(f'{numero} é divisivel por 3')
elif (numero % 5) == 0:
    print(f'{numero} é divisivel por 5')
else:
    print(f'{numero} não é divisivel por 3 e nem por 5 !!!')
