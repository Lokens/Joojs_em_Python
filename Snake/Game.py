
import pygame, sys
from pygame.locals import *
from random import randint
#fazer classe pilha 
#para o corpo da sneak , toda vez q ele comer add e se bater perde 1 
#vai ter pedras q não somem no mapa se bater perde 1 



#Cores
PRETO = (0,0,0)
AZUL = (0,0,255)
CorDaComida= (100,25,174)

#Tamanho da janela
COMPRIMENTOJANELA=440
ALTURAJANELA=510

#Direccoes
CIMA = 8
BAIXO = 2
ESQUERDA=4
DIREITA=6

#Bloco (unidade de tamanho)
bloco=[18,18]

#Quadrado
#funcao rect(X, Y, largura, altura)
#Snake
         # x   y   da cobra
snake = [(30,120),(10,120)]

cabeca = [30,120] 

x=randint(0,20)
y=randint(0,19)

comida = 0
while True:
    x1=randint(0,20)
    y1=randint(0,17)
    comidaXY=[int(x1*20)+10,int(y1*20)+120]
    if snake.count(comidaXY)==0:
        comida=1
        break

#Direcçao inicial
direccao = DIREITA

morto = 0

pontos=0

#Cria o objecto BACKGROUND
fundoJanela=pygame.display.set_mode((COMPRIMENTOJANELA,ALTURAJANELA),0,32)

#Caption da janela
pygame.display.set_caption('Snake The Game')

#set up
pygame.init()
mainClock=pygame.time.Clock()

#add maça podre
apple = pygame.Surface ((10,10))
apple.fill((255,255,255))
apple_pos = random.randint((0,400), random.randint(0,200))

while True:
    #Vemos se o evento QUIT ocorreu
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
        #Verifica as mudanças de direcçao validas
            if (event.key == K_LEFT and direccao!=DIREITA):
                    direccao=ESQUERDA
            if (event.key == K_RIGHT and direccao!=ESQUERDA):
                    direccao=DIREITA
            if (event.key == K_UP and direccao!=BAIXO):
                    direccao=CIMA
            if (event.key == K_DOWN and direccao!=CIMA):
                    direccao=BAIXO

        #<ESC> para sair do jogo
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    #Calcular o movimento da cabeca
    if direccao==DIREITA:
        cabeca[0]+=20
        if cabeca[0] > COMPRIMENTOJANELA-20:
            morto=1
    if direccao==ESQUERDA:
        cabeca[0]-=20
        if cabeca[0] < 10:
            morto=1
    if direccao==CIMA:
        cabeca[1]-=20
        if cabeca[1] < 110:
            morto=1
    if direccao==BAIXO:
        cabeca[1]+=20
        if cabeca[1] > ALTURAJANELA-30:
            morto=1

    #Se estamos a comer alguma parte do corpo morremos
    if snake.count(cabeca)>0:
         morto=1

    #Cria nova maca fora do corpo da serpente
    if comida == 0:
        while True:
            x1=randint(0,20)
            y1=randint(0,17)
            comidaXY=[int(x1*20)+10,int(y1*20)+120]
            if snake.count(comidaXY)==0:
                comida=1
                break

    #Insere a cabeca
    snake.insert(0,list(cabeca))

    #Se a cabeca tiver as mms coordenadas que a comida entao...
    if cabeca[0]==comidaXY[0] and cabeca[1]==comidaXY[1]:
        comida=0
        pontos+=5
    else:
        #remove a cauda
        snake.pop()

    #preenche o fundo
    fundoJanela.fill(PRETO)

    #Fundo scoreboard
    pygame.draw.rect(fundoJanela,AZUL,Rect([10,10],[420,100]),1)

    #Texto
    font = pygame.font.Font(None, 36)
    text = font.render("Pontos: " + str(pontos), 1, (200, 200, 200))
    textpos = text.get_rect()
    textpos.left = 75
    textpos.top = 45
    fundoJanela.blit(text, textpos)
    
    #Fundo jogo
    pygame.draw.rect(fundoJanela,AZUL,Rect([10,120],[420,380]),1)

    #desenha a serpente
    for x in snake:
        pygame.draw.rect(fundoJanela,AZUL, Rect(x,bloco))
    
    #desenha a comida
    pygame.draw.rect(fundoJanela,(CorDaComida),Rect(comidaXY,bloco))


	#parte da maça
	#screen.blit(apple,apple_pos)
	pygame.draw.rect(apple,(255,255,255),apple_pos)
    #desenha os objectos no ecra
    pygame.display.update()
    mainClock.tick(9) #FPS  