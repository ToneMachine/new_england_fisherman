import pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode((800, 600))

# Create sprite dictionaries
moving_sprite = {
    'image': pygame.image.load("pygames/graphic/npc/nemo.png"),
    'rect': pygame.Rect(100, 100, 32, 32),  # Rect for position and size
}

target_sprite = {
    'image': pygame.image.load("pygames/graphic/npc/fish.png"),
    'rect': pygame.Rect(500, 300, 32, 32),
}

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate direction
    dx = target_sprite['rect'].x - moving_sprite['rect'].x
    dy = target_sprite['rect'].y - moving_sprite['rect'].y
    length = max(abs(dx), abs(dy))
    direction = (dx / length, dy / length)

    # Move the sprite
    speed = 2
    moving_sprite['rect'].x += direction[0] * speed
    moving_sprite['rect'].y += direction[1] * speed

    # Draw sprites
    screen.fill((0, 0, 0))  # Clear the screen
    screen.blit(moving_sprite['image'], moving_sprite['rect'])
    screen.blit(target_sprite['image'], target_sprite['rect'])

    pygame.display.update()
    clock.tick(60)

pygame.quit()
