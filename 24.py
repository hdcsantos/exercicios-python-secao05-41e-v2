print('Valor de venda por estado')

uf = input("Qual o estado destino (MG, SP, RJ, MS)? ").upper()
prod = float(input("Qual valor do produto R$? "))


if uf == "MG":
    preco_final = prod + (prod * 7) / 100
    print(f"Preço final de venda para MG é R$ {preco_final}")
elif uf == "SP":
    preco_final = prod + (prod * 12) / 100
    print(f"Preço final de venda para SP é R$ {preco_final}")
elif uf == "RJ":
    preco_final = prod + (prod * 15) / 100
    print(f"Preço final de venda para RJ é R$ {preco_final}")
elif uf == "MS":
    preco_final = prod + (prod * 8) / 100
    print(f"Preço final de venda para MS é R$ {preco_final}")
else:
    print("Estado inválido !!!")

print("Fim do programa !!!")
