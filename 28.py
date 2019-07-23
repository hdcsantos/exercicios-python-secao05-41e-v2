import medias

print("Calculo de médias")
print("Informe uma das opcoes de médica, para cálculo:\n"
      "a - Geométrica\n"
      "b - Ponderada\n"
      "c - Harmonica\n"
      "d - Aritimética")
opcao = input("Opção: ")

x = float(input("Informe x: "))
y = float(input("Informe y: "))
z = float(input("Informe z: "))

if opcao == 'a':
    media = medias.geometrica(x, y, z)
    print(f'Media da opcao "a": {media}')
elif opcao == "b":
    media = medias.ponderada(x, y, z)
    print(f'Media da opcao "b": {media}')
elif opcao == 'c':
    media = medias.harmonica(x, y, z)
    print(f'Media da opcao "c": {media}')
elif opcao == 'd':
    media = medias.aritimetica(x, y, z)
    print(f'Media da opcao "a": {media}')
else:
    print("Opcao invalida, faça novamente !!!")
