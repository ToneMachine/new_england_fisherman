import pygame
from sys import exit

#systems
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("movement test")
clock = pygame.time.Clock()

#player location
playerx = 100
playery = 200
playerYmove = 0
playerXmove = 0

#surfaces
background = pygame.image.load('pygames/graphic/surface/grass_surfaces.png').convert()
player_img = pygame.image.load('pygames/graphic/npc/fish.png').convert_alpha()
player_rect = player_img.get_rect(center = (playerx,playery))

#player function
def player(x,y):
    player_rect = player_img.get_rect(center = (x,y))
    screen.blit(player_img,(player_rect))
    pygame.draw.line(screen,'black',(player_rect.midright),pygame.mouse.get_pos(), 2)

#enemy test
nemo_x = 700
nemo_y = 200
nemo_npc = pygame.image.load('pygames/graphic/npc/nemo.png').convert_alpha()

def nemo(x,y):
    nemo_rect = nemo_npc.get_rect(center = (x,y))
    screen.blit(nemo_npc,(nemo_rect))


    mouse_pos = pygame.mouse.get_pos()
    if nemo_rect.collidepoint(mouse_pos):
        detect = pygame.mouse.get_pressed()
        if detect:
            nemo_x - playerx

#game running loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #keystroke
        #keys being press down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXmove = -5
            if event.key == pygame.K_RIGHT:
                playerXmove = +5
            if event.key == pygame.K_UP:
                playerYmove = -5
            if event.key == pygame.K_DOWN:
                playerYmove = +5
        #keys being release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXmove = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYmove = 0
    
    #loop movement
    playery += playerYmove
    playerx += playerXmove
    
    #boundaries
    if playerx <= 50:
        playerx = 50
    elif playerx >= 750:
        playerx = 750
    
    if playery <= 25:
        playery = 25
    elif playery >= 375:
        playery = 375

    #surfaces being draw
    screen.blit(background,(0,0))
    
    nemo(nemo_x,nemo_y)
    player(playerx,playery)

    pygame.display.update()
    clock.tick(60)