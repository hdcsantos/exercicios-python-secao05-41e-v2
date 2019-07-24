"""
segundo grau
Uma equação do 2º grau possui a seguinte lei de formação: ax² + bx + c = 0 onde a=1, b=-2, c=-3
Δ = b²-4*a*c
x = -b +- raiz quadrada de Δ / 2*a
"""
import math

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if not a != 0:
    print("Não existe equação de segundo grau! Programa encerrado !!!")
else:
    # delta = b**2 - 4*a*c
    delta = pow(b, 2) - 4 * a * c
    print("Valor de delta é: " + str(delta))
    if delta < 0:
        print(f"Nas resoluções em que o valor do discriminante (delta) é menor que zero ({delta}), isto é,\n"
              "o número é negativo, a equação não possui raízes reais. Programa encerrado !!!")
    elif delta == 0:
        # raiz_delta = math.sqrt(delta)
        x1 = ((-b) + (delta ** 0.5)) / (2 * a)
        print(f"Raiz única x' = x'' = {x1}")
        print("Fim do programa !!!")
    elif delta >= 0:
        x1 = ((-b) + (delta ** 0.5))/(2 * a)
        x2 = (-b - (math.sqrt(delta))) / (2 * a)
        print("Valor de raiz x' = " + str(x1))
        print("Valor de raiz x'' = " + str(x2))
        print("Fim do programa !!!")
