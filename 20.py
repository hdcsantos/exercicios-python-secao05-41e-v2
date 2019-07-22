print('Lado dos triangulos')
a = int(input('Infome o valor do lado a: '))
b = int(input('Infome o valor do lado b: '))
c = int(input('Infome o valor do lado c: '))

if (b + c) > a and (c + a) > b and (a + b) > c :
    print('De acordo com as medidas, vc criou um triângulo !!!')
    if a == b and b == c and c == a:
        print('O triangulo criado é equilátero')
    elif a == b or c == a or b == c:
        print('O triangulo criado é isóceles')
    elif a != b and b != c and c != a:
        print('O triangulo criado é escaleno')
else:
  print('De acordo com as medidas, vc não criou um triângulo !!!')
