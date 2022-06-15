import pygame
from pygame import draw
from pygame.locals import *
import math
import sys as sus

SCREEN = Rect(0,0,960,720)
PlayerRegion = Rect(40,20,560,680)

class Jiki(pygame.sprite.Sprite):

    #Move_Speed = 10.0

    def __init__(self,filename,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image = pygame.image.load(filename).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x,y,width,height)

        self.fx = float(self.rect.x)
        self.fy = float(self.rect.y)
        self.dx = 0.0
        self.dy = 0.0

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LSHIFT]:
            self.Move_Speed = 4.0
        else:
            self.Move_Speed = 8.0

        if pressed_keys[K_RIGHT]:
            if pressed_keys[K_DOWN] or pressed_keys[K_UP]:
                self.fdx = 0.5**0.5 * self.Move_Speed
            else:
                self.fdx = self.Move_Speed
        elif pressed_keys[K_LEFT]:
            if pressed_keys[K_DOWN] or pressed_keys[K_UP]:
                self.fdx = 0.5**0.5 * -self.Move_Speed
            else:
                self.fdx = -self.Move_Speed
        else:
            self.fdx = 0.0
        if pressed_keys[K_DOWN]:
            if pressed_keys[K_RIGHT] or pressed_keys[K_LEFT]:
                self.fdy = 0.5**0.5 * self.Move_Speed
            else:
                self.fdy = self.Move_Speed
        elif pressed_keys[K_UP]:
            if pressed_keys[K_RIGHT] or pressed_keys[K_LEFT]:
                self.fdy = 0.5**0.5 * -self.Move_Speed
            else:
                self.fdy = -self.Move_Speed
        else:
            self.fdy = 0.0

        self.fx += self.fdx
        self.fy += self.fdy

        self.rect.x = int(self.fx)
        self.rect.y = int(self.fy)
        
        if not PlayerRegion.contains(self.rect):
            self.rect.clamp_ip(PlayerRegion)
            self.fx = self.rect.x
            self.fy = self.rect.y



class main:
    pygame.init()
    screen = pygame.display.set_mode(SCREEN.size)
    pygame.display.set_caption("SUPER SPRITE TEST")

    group = pygame.sprite.RenderUpdates()
    Jiki.containers = group

    test = Jiki("test.png",300,600)

    clock = pygame.time.Clock()
    while 1:
        clock.tick(60)
        screen.fill((200,255,255))
        draw.rect(screen,(0,0,0),PlayerRegion)
        group.update()
        group.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sus.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sus.exit()



if __name__ == "__main__":
    main()