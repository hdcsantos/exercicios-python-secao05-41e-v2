print("Km/l")

km = int(input("informe a quilometragem: "))
litro = int(input("Quatidade de litros consumidos no percurso: "))

media = km / litro
print(media)
if media < 8:
    print("Venda o carro !!!")
elif 8 <= media <= 14:
    print("Economico !!!")
elif media > 12:
    print("Super Economico !!!")
