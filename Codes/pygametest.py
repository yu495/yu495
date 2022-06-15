import pygame,sys
from pygame.locals import * #ていすうぜんぶよみこむ！

pygame.init() #たぶんinitializeのこと

size = width, height = 600, 480 #画面のサイズ
screen = pygame.display.set_mode(size)

title = "Hi are ya doin well" #タイトル
pygame.display.set_caption(title)

font = pygame.font.Font(None,70)

while 1: # i n f l o o pを起こす
    screen.fill((255,255,255)) #塗りつぶし
    text1 = font.render("I", True, (0,0,0))
    text2 = font.render("Will", True, (0,0,0))
    text3 = font.render("Be", True, (0,0,0))
    text4 = font.render("Right", True, (0,0,0))
    text5 = font.render("Back", True, (0,0,0))
    screen.blit(text1,(20,10))
    screen.blit(text2,(20,60))
    screen.blit(text3,(20,110))
    screen.blit(text4,(20,160))
    screen.blit(text5,(20,210))



    pygame.display.update()

    #イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()