print('Area de um trapézio')

base_maior = float(input("Tamanho da base maior: "))
base_menor = float(input("Tamanho da base menor: "))
altura = float(input("Altura: "))

if base_maior <= 0 or base_menor <= 0:
    print("Informe valores nas bases, maior que 0 (zero) !!!")
else:
    area = (base_menor + base_maior) * altura / 2
    print(f'A área do trapézio de de {area}')

print("programa encerrado!!!")
# teste linha 14 ok ok
# beleza
# do remoto para local
# do local para remoto
