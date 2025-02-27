import pygame
import sys

# Initialize Pygame
pygame.init()

# Updated screen dimensions for a larger area
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platformer with Platforms, Spikes, and Higher Jump")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 50, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)

# Player properties
player_width = 50
player_height = 50
player_x = 100  # Start near the far left side of the screen
player_y = SCREEN_HEIGHT - player_height - 50  # On top of the ground
player_velocity = 5
jump_velocity = 20  # Increased jump height
fall_velocity = 0

# Game clock
clock = pygame.time.Clock()

# Ground and wall properties
ground_height = 100
wall_thickness = 50  # Thickness of walls on left and right

# Spike properties
spike_width = 50
spike_height = 20
spikes = [(600, SCREEN_HEIGHT - ground_height - spike_height),
          (900, SCREEN_HEIGHT - ground_height - spike_height),
          (1100, SCREEN_HEIGHT - ground_height - spike_height)]  # Updated spike positions

# Platform properties (x, y, width, height)
platforms = [
    pygame.Rect(200, 600, 200, 20),  # Platform 1
    pygame.Rect(500, 500, 200, 20),  # Platform 2
    pygame.Rect(800, 400, 200, 20),  # Platform 3
    pygame.Rect(300, 300, 200, 20)   # Platform 4
]

# Game loop
running = True
on_ground = False
while running:
    screen.fill(WHITE)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()

    # Horizontal movement (check left and right walls)
    if keys[pygame.K_LEFT] and player_x > wall_thickness:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width - wall_thickness:
        player_x += player_velocity

    # Jumping and gravity
    if keys[pygame.K_SPACE] and on_ground:
        fall_velocity = -jump_velocity  # Set the jump velocity (going upwards)
        on_ground = False

    # Apply gravity
    fall_velocity += 1
    player_y += fall_velocity

    # Collision with the ground
    if player_y >= SCREEN_HEIGHT - player_height - ground_height:
        player_y = SCREEN_HEIGHT - player_height - ground_height
        fall_velocity = 0
        on_ground = True

    # Collision with platforms
    on_platform = False
    for platform in platforms:
        if platform.colliderect(pygame.Rect(player_x, player_y + fall_velocity, player_width, player_height)):
            if fall_velocity >= 0:  # Only land when falling down
                player_y = platform.top - player_height
                fall_velocity = 0
                on_platform = True
                break

    if not on_platform:
        on_ground = False

    # Collision with the top wall
    if player_y < 0:
        player_y = 0
        fall_velocity = 0

    # Collision with spikes (reset the player if hit)
    for spike in spikes:
        spike_rect = pygame.Rect(spike[0], spike[1], spike_width, spike_height)
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        if player_rect.colliderect(spike_rect):
            # Reset the player to the starting position if they hit a spike
            player_x = 100  # Starting from the far left
            player_y = SCREEN_HEIGHT - player_height - 50  # On top of the ground
            fall_velocity = 0
            on_ground = True
            print("Player hit a spike! Resetting position.")

    # Draw the player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    # Draw the ground
    pygame.draw.rect(screen, BLACK, (0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height))

    # Draw the walls
    pygame.draw.rect(screen, RED, (0, 0, wall_thickness, SCREEN_HEIGHT))  # Left wall
    pygame.draw.rect(screen, RED, (SCREEN_WIDTH - wall_thickness, 0, wall_thickness, SCREEN_HEIGHT))  # Right wall

    # Draw the spikes
    for spike in spikes:
        pygame.draw.polygon(screen, GREEN, [
            (spike[0], spike[1]),  # Left base of the spike
            (spike[0] + spike_width // 2, spike[1] - spike_height),  # Top of the spike
            (spike[0] + spike_width, spike[1])  # Right base of the spike
        ])

    # Draw the platforms
    for platform in platforms:
        pygame.draw.rect(screen, BROWN, platform)

    # Update the display
    pygame.display.flip()

    # Frame rate (FPS)
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
