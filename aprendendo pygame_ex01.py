#importando as blibiotecas.
import pygame
import pygame.display
from pygame.locals import *
from sys import exit

#iniciando o pygame.
pygame.init()

# Definindo o tamanho da janela do jogo.
largura = 640
altura = 480


tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Solo leveling')

# Fazendo um loop para o jogo poder se atualizar automaticamente quando o jogo iniciar.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,0,0), (200,300,40,50))
    pygame.draw.circle(tela, (255,255,0), (300,260), 40)
    pygame.draw.line(tela, (0,0,255), (390,0), (390,600), 5)
    pygame.display.update()