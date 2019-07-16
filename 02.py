import math

print("Raiz quadrada")

n = int(input("Número: "))

if n > 0:
    # raiz = n ** 0.5
    raiz = math.sqrt(n)
    print(f'Raiz quadrada de {n} é {raiz}')
else:
    print(f'{n} é inválido')
