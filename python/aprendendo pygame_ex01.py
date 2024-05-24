#importando as blibiotecas.
import pygame
import pygame.display
from pygame.locals import *
from sys import exit
from random import randint

#iniciando o pygame.
pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('short-8-bit-background-music-for-video-mobile-game-old-school-37sec-164704.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

# Definindo o tamanho da janela do jogo.
largura = 640
altura = 480
x_snake = int(largura/2)
y_snake = int(altura/2)   

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game 0.1')
relogio = pygame.time.Clock()
lista_snake = []
comprimento_inicial = 5
morreu = False

def aumenta_snake(lista_snake):
    for XeY in lista_snake:
        #XeY = [x, y]
        #XeY[0] = x
        #XeY[1] = y

        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))

def reiniciar_jogo():
    global pontos, comprimento_inicial, x_snake, y_snake, lista_snake, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5
    x_snake = int(largura/2)
    y_snake = int(altura/2)
    lista_snake = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False

# Fazendo um loop para o jogo poder se atualizar automaticamente quando o jogo iniciar.
while True:
    relogio.tick(30)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    testo_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0  

    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle

    snake = pygame.draw.rect(tela, (0,255,0), (x_snake,y_snake,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))

    if snake.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
    
    lista_cabeca = []
    lista_cabeca.append(x_snake)
    lista_cabeca.append(y_snake)

    lista_snake.append(lista_cabeca)

    if lista_snake.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, bold=True, italic=True)
        mensagem = 'Game Over! Pressione a tecla R para jogar novamente'
        testo_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = testo_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(testo_formatado, ret_texto)
            pygame.display.update()

    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake < 0:
        y_snake = altura
    if y_snake > altura:
        y_snake = 0

    if len(lista_snake) > comprimento_inicial:
        del lista_snake[0]

    aumenta_snake(lista_snake)

    tela.blit(testo_formatado, (450,40))
    pygame.display.update()