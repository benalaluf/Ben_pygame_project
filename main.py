import pygame

# Initialize Pygame
pygame.init()

# Set screen size and caption
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moon Jump")

# Load player image
player_image = pygame.image.load("graphics/link.png")
player_image = pygame.transform.scale(player_image, (40, 40))

font = pygame.font.Font(None, 50)
text_srf = font.render("The Moon:", False, 'white')

# Set player starting position and velocity
player_x = 50
player_y = 50
player_velocity_x = 0
player_velocity_y = 0

# Set Moon's gravity force
moon_gravity = 0.1

# Set player's movement speed
player_speed = 4

# Set player's jumping force
jumping_force = -10

# Set floor position
floor_y = 550

# check if player is jumping
jumping = False

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_velocity_x = -player_speed
            if event.key == pygame.K_RIGHT:
                player_velocity_x = player_speed
            if event.key == pygame.K_SPACE:
                if not jumping:
                    jumping = True
                    player_velocity_y = jumping_force
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_velocity_x = 0

    # Move player based on velocity
    player_x += player_velocity_x
    player_y += player_velocity_y

    # Apply Moon's gravity force to player
    player_velocity_y += moon_gravity

    # Check for collision with floor
    if player_y > floor_y - player_image.get_height():
        player_y = floor_y - player_image.get_height()
        player_velocity_y = 0
        jumping = False

    if player_x > 760:
        player_x = 760

    if player_x < 0:
        player_x = 0
    # Clear screen
    screen.fill((0, 0, 0))

    # Draw floor
    pygame.draw.rect(screen, (255, 255, 255), (0, floor_y, 800, 50))

    # Draw player
    screen.blit(player_image, (player_x, player_y))
    screen.blit(text_srf,(300,200))

    # Update display
    pygame.display.update()

# Quit Pygame
