import math

print("Número real")

n = int(input("Número: "))

if n > 0:
    # raiz = n ** 0.5
    raiz = math.sqrt(n)
    print(f'Raiz quadrada de {n} é {raiz}')
else:
    quadrado = n ** 2
    # quadrado = math.pow(n ,2)
    print(f'Quadrado de {n} é {quadrado}')
