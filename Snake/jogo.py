#versão Beta 1.0

#jogo do trabalho do emilio para estrutura de dados 2 
#espero que esteja tudo certo


import pygame,random
from pygame.locals import *


pygame.init()

#altuta e janelinha da tela
Altura = 600
Largura =  600
screen = pygame.display.set_mode ((Altura , Largura))

#nome da tela
pygame.display.set_caption('Cobrinha')

#função pra retornar uma posição por 10
#exemplo pra 209 -> 210
def on_grid_random():
	X = random.randint(0,590)
	Y = random.randint(0,590)
	return (X//10 * 10, Y//10 *10)
	

def colisao(obj1,obj2):
	return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])  

	
#direçoes
UP = 0
RIGHT = 1
DOWN = 2 
LEFT = 3

#corpo da cobra
#cobra é um vetor de tuplas 
snake = [(200,200) , (210,200) , (220,200)]
snake_skin = pygame.Surface((10,10))

CorDaCobra= (255,255,255)
snake_skin.fill(CorDaCobra)

Direção = RIGHT

Velocidade = 10
if Velocidade < 10:
	Velocidade = 10

print (Velocidade)
#criação da comida
Pos_Comida = on_grid_random()
CorDaComida = (0,255,0)						
						#taanho da coisa
comida = pygame.Surface((10,10))

comida.fill(CorDaComida)

#criação da comida que diminui a velocidade
Pos_Comida2 = on_grid_random()
CorDaComida2 = (255,0,0)
comida2 = pygame.Surface((10,10))
comida2.fill(CorDaComida2)


#fps
FPS = pygame.time.Clock()


while True :
	#velocidade do game FPS
	FPS.tick(Velocidade)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
	
	

			
	#teclas de movimento 
		if event.type == KEYDOWN:
			if event.key == K_UP:
				Direção = UP
			if event.key == K_DOWN:
				Direção = DOWN
			if event.key == K_LEFT:
				Direção = LEFT
			if event.key == K_RIGHT:
				Direção = RIGHT
	
	if Velocidade < 10:
		Velocidade = 10
		
		
	print(snake)
		
	#colisao da comida que almente a velocidade
	if colisao(snake[0],Pos_Comida):
		Pos_Comida = on_grid_random()
		
		#novo quadrado da cobra 
		#não importa ser 0,0 pq ela vai pegar a posição q o rabo tinha 
		snake.append((0,0))
		Velocidade = Velocidade + 5
		
	
	#colisao da comida q diminui a velocida
	if colisao(snake[0],Pos_Comida2):
		Pos_Comida2 = on_grid_random()
		#novo quadrado da cobra 
		#não importa ser 0,0 pq ela vai pegar a posição q o rabo tinha 
		#snake.append((0,0))
		#Velocidade = Velocidade - 15
		snake.pop(len(snake)-1)
		
	#colisao para morrer encostando, incacabada	
	#if snake.count(cabeca)>0:
        #Morto = True
	
	
	#começa a ler a cobra de traz pra frete 
	#fazendo com q o quadrado mais a esquerda ocupe o lugar 
	#onde estava o quadrado da direita
	for i in range(len(snake) -1,0,-1):
		snake[i] = (snake[i-1][0], snake[i-1][1])
			
			
			
	#direção da cobra 
	#sempre vai se mecher pra onde ta "olhando"
	if Direção == UP :
		snake[0] = (snake[0][0],snake[0][1] -10 )
	if Direção == DOWN :
		snake[0] = (snake[0][0], snake[0][1] +10 )	
	if Direção == RIGHT :
		snake[0] = (snake[0][0] +10 , snake[0][1])
	if Direção == LEFT :
		snake[0] = (snake[0][0] -10 , snake[0][1])	
	
	
	
	screen.fill((0,0,0))
	
	#comida na tela 
	screen.blit(comida, Pos_Comida)
	#comida2 na tela 
	screen.blit(comida2, Pos_Comida2)
	
	
	for pos in snake :
		screen.blit(snake_skin,pos)
			
	pygame.display.update()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#veio aqui atoa
#TROXÃO
#huehuehue	