import math

print('Logaritimo de numero positivo')

logaritimando = int(input('Informe um numero: '))

if logaritimando < 0:
    print('Número inválido')
else:
    logaritimo = math.log1p(logaritimando)
    print(f'Logaritimo de {logaritimando} é {int(logaritimo)}')
