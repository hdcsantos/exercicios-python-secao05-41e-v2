print("Empréstimo trabalhador")

sal = float(input("Salário: "))
prestacao = float(input("Valor da prestação: "))

if prestacao >= sal * 0.20:
    print('Empréstimo não concedido!')
else:
    print('Empréstimo concedido!')
