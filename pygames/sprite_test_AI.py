import pygame
from sys import exit

#systems
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Sprite test done with AI")
clock = pygame.time.Clock()

#background image
background = pygame.image.load('pygames/graphic/surface/grass_surfaces.png').convert()

#player location
x = 400
y = 200

#player class
class sprite_player(pygame.sprite.Sprite):
    #player sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pygames/graphic/npc/fish.png').convert_alpha()
        self.rect = self.image.get_rect(center = (x,y))
        self.speed = 5

    #player movement
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Limit player movement within screen boundaries
        self.rect.x = max(0, min(self.rect.x, 800 - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, 400 - self.rect.height))

#Create sprite objects:
player = sprite_player()

#Create a sprite group and add the sprite to it
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#game running loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #creat background
    screen.blit(background,(0,0))

    #Update sprite positions or perform other game logic here
    all_sprites.update()

    # Draw the sprites on the screen
    all_sprites.draw(screen)

    # Update the display
    pygame.display.update()
    clock.tick(60)   