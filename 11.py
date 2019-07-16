print("Soma de todos os algarismos")

numero = int(input('Informe um número: '))

if numero > 0:
    numero_lista = list(range(3))
    numero_lista[0] = numero // 100
    numero_lista[1] = numero // 10 - 10 * (numero//100)
    numero_lista[2] = numero - 10 * (numero // 10 - 10 * (numero // 100)) - 100 * (numero // 100)
    print(numero_lista)
    resultado = numero_lista[0] + numero_lista[1] + numero_lista[2]
    print(f'A soma de {numero_lista[0]} + {numero_lista[1]} + {numero_lista[2]} é igual {resultado}')
else:
    print('Número inválido')
