print('Lado dos triangulos')
a = int(input('Infome o valor do lado a: '))
b = int(input('Infome o valor do lado b: '))
c = int(input('Infome o valor do lado c: '))

if a < (b + c) and b < (c + a) and c < (a + b):
    print('De acordo com os valores, vc criou um triângulo! Agora vamos saber qual é o seu tipo.')
    if a == b and b == c and c == a:
        print('O triangulo criado é equilátero, pois seus tres lados são iguais!')
    elif a == b or c == a or b == c:
        print('O triangulo criado é isóceles, pois dois de seus lados são iguais!')
    else:  # elif a != b and b != c and c != a:
        print('O triangulo criado é escaleno, pois seus tres lados são difeirentes!')
else:
    print('De acordo com as medidas, vc não criou um triângulo !!!!')
