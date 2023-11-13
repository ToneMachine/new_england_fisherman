import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Fishing")
clock = pygame.time.Clock()

#background
ocean_surface = pygame.image.load('pygames/graphic/surface/background1.png').convert()

#score surface
score_font = pygame.font.Font(None, 30)
score_surf = score_font.render('Score: 0', True, 'White')
score_rect = score_surf.get_rect(topleft = (20,10))

#player sprite
playerx = 400
playery = 90
player_x_move = 0
player_img = pygame.image.load('pygames/graphic/npc/fisherman.png').convert_alpha()

def player(x,y):
    player_rect = player_img.get_rect(midbottom = (x,y))
    screen.blit(player_img,(player_rect))
    pygame.draw.line(screen,'black',(player_rect.topright),pygame.mouse.get_pos(), 2)                                

#cursor/hook
pygame.mouse.set_visible(False)

#lobster rect
lobster_npc = pygame.image.load('pygames/graphic/npc/lobster.png').convert_alpha()
lobster_rect = lobster_npc.get_rect(topleft = (750, 350))

#clown fish sprite
nemo_x = 400
nemo_y = 200
nemo_npc = pygame.image.load('pygames/graphic/npc/nemo.png').convert_alpha()

def nemo(x,y):
    nemo_rect = nemo_npc.get_rect(center = (x,y))
    screen.blit(nemo_npc,(nemo_rect))

    mouse_pos = pygame.mouse.get_pos()
    if nemo_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #player inputs
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_move -= 5
            elif event.key == pygame.K_a:
                player_x_move -= 5
            
            if event.key == pygame.K_RIGHT:
                player_x_move += 5
            elif event.key == pygame.K_d:
                player_x_move += 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or pygame.K_a or event.key == pygame.K_RIGHT or pygame.K_d:
                player_x_move = 0  

    playerx += player_x_move             

    #boundaries
    if playerx <= 50:
        playerx = 50
    elif playerx >= 775:
        playerx = 775

    #background
    screen.blit(ocean_surface,(0,0))

    #score board
    pygame.draw.rect(screen,'Black',score_rect)
    screen.blit(score_surf,(score_rect))

    #lobster
    screen.blit(lobster_npc,(lobster_rect))
    lobster_rect.left -= 3
    if lobster_rect.right <= 0:
        lobster_rect.left = 800
    
    #clown fish
    nemo_x += 2
    if nemo_x >= 900:
        nemo_x = 0
    nemo(nemo_x,nemo_y)

    #player/fishermen
    player(playerx,playery)
    
    #mouse boolean
    mouse_pos = pygame.mouse.get_pos()
    if lobster_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)