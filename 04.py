import math

print("Número quadrado e raiz")

n = int(input("Número: "))

if n > 0:
    quadrado = n ** 2
    # quadrado = math.pow(n ,2)
    # raiz = n ** 0.5
    raiz = math.sqrt(n)
    print(f'Raiz quadrada de {n} é {raiz} e {n} elevado a 2 é {quadrado}')
else:
    print('Valor inválido')
