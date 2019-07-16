print("Qual numero é maior")

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print(f'Primeiro número é maior')
elif n1 == n2:
    print(f'Os números são iguais')
else:
    print(f'Segundo número é maior')
