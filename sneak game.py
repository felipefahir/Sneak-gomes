import pygame
from pygame.locals import *
from sys import exit
from random import randint
from time import sleep
pygame.init()


pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('Sneak-game\music.wav')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('Sneak-game\jump.wav')

largura = 640
altura = 480

x_cobra = int(largura/2) 
y_cobra = int(altura/2)

velocidade = 10
x_controle = velocidade
y_controle = 0


x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5
morreu = False

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, x_maca, y_cobra, y_maca, morreu, lista_cabeca, lista_cobra
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2) 
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False


while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
       
        
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_RIGHT:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_UP:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_DOWN:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
        
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))
    sima = pygame.draw.rect(tela, (0,100,100), (0 ,10,largura, 20))
    baixo = pygame.draw.rect(tela, (0,100,100), (0,465 ,largura, 20))
    direito = pygame.draw.rect(tela, (0,100,100), (620,10 ,20, altura))
    esquerdo = pygame.draw.rect(tela, (0,100,100), (0 , 10,20, altura))



    if cobra.colliderect(sima):
        morreu = True
        while morreu:
            tela.fill((255, 200, 200))
            msg_one = 'Si lascou, perta R ai'
            msg_one_plus = fonte.render(msg_one, True, (0, 0, 0))
            tela.blit(msg_one_plus, (60, 240))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()    
            pygame.display.update()

    if cobra.colliderect(direito):
        morreu = True
        while morreu:
            tela.fill((255, 200, 200))
            msg_one = 'Si lascou, perta R ai'
            msg_one_plus = fonte.render(msg_one, True, (0, 0, 0))
            tela.blit(msg_one_plus, (60, 240))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()    
            pygame.display.update()

    if cobra.colliderect(baixo):
        morreu = True
        while morreu:
            tela.fill((255, 200, 200))
            msg_one = 'Si lascou, perta R ai'
            msg_one_plus = fonte.render(msg_one, True, (0, 0, 0))
            tela.blit(msg_one_plus, (60, 240))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()    

            pygame.display.update()                
    if cobra.colliderect(esquerdo):
        morreu = True
        while morreu:
            tela.fill((255, 200, 200))
            msg_one = 'Si lascou, perta R ai'
            msg_one_plus = fonte.render(msg_one, True, (0, 0, 0))
            tela.blit(msg_one_plus, (60, 240))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()    

            pygame.display.update()



    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    
    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True
        while morreu:
            tela.fill((255, 200, 200))
            msg_one = 'Si lascou, perta R ai'
            msg_one_plus = fonte.render(msg_one, True, (0, 0, 0))
            tela.blit(msg_one_plus, (60, 240))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()    

            pygame.display.update()


    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)
    
    tela.blit(texto_formatado, (240,40))

    
    pygame.display.update()