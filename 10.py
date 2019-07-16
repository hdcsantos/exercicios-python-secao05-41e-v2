print("Peso ideal")

sexo = input('Qual seu genero (H ou M)? ')
h = float(input("Altura: "))
peso = float(input("Peso: "))

if sexo == 'H':
    p_i = ((72.7 * h) - 58) // 1
    print(f'Seu peso ideal é de {p_i} Kg!')
else:
    p_i = ((62.1 * h) - 44.7) // 1
    print(f'Seu peso ideal é de {p_i} Kg!')
