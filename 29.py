"""import random

# constantes
MENOR = 1     # limite inferior (inclusive) de um número sorteado
MAIOR = 100   # limite superior (exclusive) de um número sorteado
TAMANHO_DA_SEQ = 5   # tamanho da sequência sorteada

def main():
    ''' Programa que sorteia 5 inteiros entre 0 e 99.
    '''
    semente = int(input("Digite a semente: "))
    random.seed(semente)   ## inicializa o gerador com a semente

    cont = 0
    while cont < TAMANHO_DA_SEQ:
        sorteio = random.randrange(MENOR, MAIOR)
        cont += 1
        print( 'Sorteio', cont, ':', sorteio )

if __name__ == '__main__':
    main()"""
from random import randint
import op_matematicas

print("Prova matematica para crianças (s para terminiar o programa)")

condicao = 'S'
while condicao == "S":
    array = []
    cont = 0
    while cont < 2:
        sorteio = randint(1, 100)
        array.append(sorteio)
        cont += 1
    print(f'Qual é a soma de {array[0]} + {array[1]} ?')
    soma = op_matematicas.soma(array[0], array[1])

    resposta = int(input("Resposta: "))

    p1 = int(input("\nQual o resultado da soma elevado ao cubo? "))
    cubo = op_matematicas.exp_cubo(soma)

    p2 = int(input("Qual o resultado da soma, multiplicado por 12? "))
    multi = op_matematicas.multiplicacao(soma, 12)

    p3 = float(input("Qual o resultado da soma, dividido por 6? "))
    div = op_matematicas.divisao(soma, 6)

    p4 = float(input("Qual a raiz quadrada da soma? "))
    raizQ = op_matematicas.raiz_quadrada(soma)

    p5 = int(input("Qual o resultado da soma, subtraido de 6? "))
    sub = op_matematicas.subtracao(soma, 6)

    if resposta == soma:
        print("\nSua soma está correta !!!")
        cont = 0
        if p1 == cubo:
            print("Sua soma, elevada ao cubo está correta !!!")
            cont += 1
        else:
            print(f"Sua soma, elevada ao cubo está incorreta, o valor correto é {cubo} !!!")
        if p2 == multi:
            print("Sua soma, multiplicada por 12 está correta !!!")
            cont += 1
        else:
            print(f"Sua soma, multiplicada por 12 está incorreta, o valor correto é {multi} !!!")
        if p3 == div:
            print("Sua soma, dividida por 6 está correta !!!")
            cont += 1
        else:
            print(f"Sua soma, dividida por 6 está incorreta, o valor correto é {div:.2f} !!!")
        if p4 == raizQ:
            print("A raiz quadrada da soma está correta !!!")
            cont += 1
        else:
            print(f"A raiz quadrada da soma está incorreta, o valor correto é {raizQ:.2f} !!!")
        if p5 == sub:
            print("Sua soma, subtraida por 6 está correta !!!")
            cont += 1
        else:
            print(f"Sua soma, subtraida por 6 está incorreta, o valor correto é {sub} !!!")
        print(f"\nVoce acertou {cont} pergunta(s) !!!")

        condicao = input("\nDeseja continuar com a avaliação (S p/ sim ou N p/ não)? ").upper()
        continue
    else:
        print(f"\nA resposta da operação de soma está incorreta, com isso, "
              "\nas respostas das outras perguntas estão incorretas também e "
              "\nelas não serão apresentadas. Sendo assim, a avaliação será reiniciada, "
              f"\ncom novos dados, até voce acertar! A reposta correta da soma era {soma} !!!\n\n")
    continue
else:
    print("Fim do programa de avaliação !!!")
