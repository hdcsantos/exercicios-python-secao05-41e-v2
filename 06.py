print("Qual numero é maior")

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))

if n1 > n2:
    print(f'{n1} é o maior número')
    d = n1 - n2
else:
    print(f'{n2} é o maior número')
    d = n2 - n1

print(f'A diferença entre {n1} e {n2} é {d}')
