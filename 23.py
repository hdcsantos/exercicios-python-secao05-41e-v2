print('Ano bissexto')

ano = int(input('Qual o ano? '))

if ano % 4 == 0 or ano % 400 == 0 or not ano % 100 != 0:
    print(f'{ano} é bissexto !!!')
