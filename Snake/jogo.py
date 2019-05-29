#versão Beta 2.0

#jogo do trabalho do emilio para estrutura de dados 2 
#espero que esteja tudo certo


import pygame,random,time
from pygame.locals import *


pygame.init()

#altuta e janelinha da tela
Largura = 720
Altura =  600
screen = pygame.display.set_mode ((Largura, Altura))

#nome da tela
pygame.display.set_caption('Cobrinha')

#função pra retornar uma posição por 10
#exemplo pra 209 -> 210
def on_grid_random():
	X = random.randint(40,640)
	Y = random.randint(100,480)
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
#snake = [(200,200) , (210,200) , (220,200)] #tamanho inicial da cobra
snake = [(200,200)]
snake_skin = pygame.Surface((10,10))

CorDaCobra = (255,255,255)
snake_skin.fill(CorDaCobra)

Direção = RIGHT

Velocidade = 10


print (Velocidade)
#criação da comida
Pos_Comida = on_grid_random()
CorDaComida = (0,255,0)						

					#tamanho da coisa
comida = pygame.Surface((10,10))

comida.fill(CorDaComida)

#criação da comida que diminui a velocidade
Pos_Comida2 = on_grid_random()
CorDaComida2 = (255,0,0)
#comida2 = pygame.Surface((30,30))
comida2 = pygame.Surface((10,10))
comida2.fill(CorDaComida2)





#pontuação

Pontos = 0

#Tela
fundoJanela=pygame.display.set_mode((Largura,Altura),0,32)

#fps
FPS = pygame.time.Clock()
comida_na_tela = 0

vida = True



while vida:
	#velocidade do game FPS
	FPS.tick(Velocidade)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			
		#<ESC> para sair do jogo
		if event.type == KEYUP:	
			if event.key == K_ESCAPE:
				pygame.quit()
	
			
	#teclas de movimento 
		if event.type == KEYDOWN:
			if event.key == K_UP:
				if Direção != DOWN:
					Direção = UP
			if event.key == K_DOWN:
				if Direção != UP:
					Direção = DOWN
			if event.key == K_LEFT:
				if Direção != RIGHT:
					Direção = LEFT
			if event.key == K_RIGHT:
				if Direção != LEFT:	
					Direção = RIGHT
			
			
	
	if Velocidade < 10:
		Velocidade = 10
		
		
	#print(snake)
		
	# COLISOES 	
		
	#colisao da comida que almente a velocidade
	if colisao(snake[0],Pos_Comida):
		Pos_Comida = on_grid_random()
		
		#novo quadrado da cobra 
		#não importa ser 0,0 pq ela vai pegar a posição q o rabo tinha 
		snake.append((0,0))
		Velocidade = Velocidade + 5
		Pontos += 25 
	
	if colisao(snake[0],Pos_Comida2):
		Pos_Comida2 = on_grid_random()
		Velocidade = 15
		if (len(snake) == 1 ):
			
			vida = False
			
			
			#snake.pop(len(snake)-1)
		else:
		
			for d in range (len(snake)//2):
				snake.pop(len(snake)-1)
		
		Pontos  = Pontos // 2
		
	
	#colisao da comida q diminui a velocide
	
	
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
	
	
	
	
	
	
	#cor da tela (preto)
	screen.fill((0,0,0))
	
	#comida na tela 
	screen.blit(comida, Pos_Comida)
	
	#comida2 na tela 
	#if pra pontuação minima para aparecer a comida vermelha 
	
	tempinho = 0.0
	teste = []
	#teste.append(comida2,Pos_Comida2)
	
	if Pontos >= 0:
		screen.blit(comida2,(Pos_Comida2))
		
		
	 
	#placar
	#escolhe a cor do que vai ser escrito
	font_color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
	
	#estilo e tamanho da letra
	font = pygame.font.Font(None, 54)
	
	
	
	#oq vai ser escrito e como 
	text = font.render(str("PONTOS : "),True ,font_color)
	text_pontos = font.render (str(Pontos), True, font_color)
	
	text_velocidade = font.render (str("velocidade : "),True, font_color)
	text_velocidade_cont = font.render (str(Velocidade),True,font_color)
	
	#coloca o letras na tela 
	screen.blit(text, (50 , 40))
	screen.blit(text_pontos,(250,40))
	
	
	screen.blit(text_velocidade,(350,40))
	screen.blit(text_velocidade_cont,(590,40))
	
	
	Tamanho_da_borda = [40, 100, 640, 480]
	pygame.draw.rect(screen, font_color, Tamanho_da_borda, 5)
	#Borda = pygame.Surface(Tamanho_da_borda)
	#Borda.fill(font_color)
	
	
	
	
		
	
	
	
	
	
	for pos in snake :
		screen.blit(snake_skin,pos)
			
			
			
			
			
	pygame.display.update()
	
"""	
if vida == False:
	Game_over= font.render (str("GAME OVER"),True, CorDaComida2)
	screen.blit(Game_over,(240,280))
	time.sleep(5)
"""


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#veio aqui atoa
#TROXÃO
#huehuehue	