#MATHEUS SLAMA RIBAS
#ALFA 1.0

import random

print('#'*56)

print('\n   BEM VINDO AO PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK. \n')

print('#'*56)


while(1):
    print(''' \nEscolha:
0-Tesoura
1-Papel
2-Pedra
3-Lagarto
4-Spock
5-Regras
6-Sair''')


    lista=['Tesoura','Papel','Pedra','Lagarto','Spock']
    jogador = int(input())
    if jogador < 0 or jogador >6 :
        print('joga direito caralho')
    elif jogador == 5:
        print('https://www.youtube.com/watch?v=abQj0pQkSOY')


    elif jogador == 6 :
        break
    else:
        maquina=random.randrange(0,4)
        print ("Maquina jogou: ",lista[maquina],'\n')

        if jogador == 0 and (maquina == 1 or maquina == 3):
            print (f'Ae carai you win \n {lista[jogador]} ganhou!!!')

        elif jogador == 1 and (maquina == 2 or maquina == 4):
            print (f'É nois mano you win \n {lista[jogador]} ganhou!!!')

        elif jogador == 2 and (maquina == 1 or maquina == 3):
            print (f'you win \'o maluco é brabo\' \n {lista[jogador]} ganhou!!!')

        elif jogador == 3 and (maquina == 4 or maquina == 1):
            print (f'mandou you win \n {lista[jogador]} ganhou!!!')

        elif jogador == 4 and (maquina == 0 or maquina == 2):
            print (f'É Spock nesse carai mermao \n {lista[jogador]} ganhou!!!')

        else :
            print("Tu Perdeu OTARIO")



