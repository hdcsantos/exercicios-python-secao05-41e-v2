print('Média ponderada')

p1, p2, p3 = 1, 1, 2
n1 = float(input('Nota na prova de Matemática: '))
n2 = float(input('Nota na prova de História: '))
n3 = float(input('Nota na prova de Português: '))

mp = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)
# b = p1 + p2 + p3
# mp = a / b

if mp >= 60:
    print(f'Aluno aprovado com média {mp} pontos')
else:
    print(f'Aluno reporvado com média {mp} pontos')
