print("Nota valida e média")

n1 = float(input("Primeiro nota: "))
n2 = float(input("Segunda nota: "))

if n1 >= 0.0 and n1 <= 10.0 and n2 >= 0.0 and n2 <= 10.0:
    media = (n1 + n2) / 2
    print(f'A média das notas é {media}!')
else:
    print('Notas de valores invalidos!')
