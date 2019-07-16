print('Media ponderada 2')

laboratorio, semestral, final = 2, 3, 5
n1 = float(input('Nota na prova de Laboratório: '))
n2 = float(input('Nota na prova de Semestral: '))
n3 = float(input('Nota na prova de Final: '))

'''
if not n1 and n2 and n3 == type(float):
  print('Notas não podem ser somente Inteiro')
'''

if not 0 <= n1 <= 10:
    print('Nota Laboratório não é valida')
elif not 0 <= n2 <= 10:
    print('Nota Semestral não é valida')
elif not 0 <= n3 <= 10:
    print('Nota Final não é valida')
else:
    media_pond = (n1 * laboratorio + n2 * semestral + n3 * final) / (laboratorio + semestral + final)

    if 0 <= media_pond <= 2.9:
        print(f'Aluno reprovado com média {media_pond}')
    elif 3 <= media_pond <= 4.9:
        print(f'Aluno está de recuperação, com média {media_pond}')
    else:
        print(f'Aluno aprovado com média {media_pond}')
