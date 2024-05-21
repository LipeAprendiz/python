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
x = int(largura/2)
y = int(altura/2)   

x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake Game 0.1')
relogio = pygame.time.Clock()

# Fazendo um loop para o jogo poder se atualizar automaticamente quando o jogo iniciar.
while True:
    relogio.tick(30)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    testo_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
       if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20'''

    if pygame.key.get_pressed()[K_a]:
        x = x - 20
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
    if pygame.key.get_pressed()[K_w]:
        y = y - 20
    if pygame.key.get_pressed()[K_s]:
        y = y + 20

    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50))
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50))

    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
    
    tela.blit(testo_formatado, (450,40))
    pygame.display.update()