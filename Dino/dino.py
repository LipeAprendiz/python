import pygame
import pygame.display
from pygame.locals import *
from sys import exit
import os

diretorio_principal = os.path.dirname()

largura = 640
altura = 480

BRANCO = (255,255,255)

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption('Dino Game')

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pass

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

relogio = pygame.time.Clock()
while True():
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()