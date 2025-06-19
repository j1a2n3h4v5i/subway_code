import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Subway Surfer Clone")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player
player_width, player_height = 50, 50
player_x = WIDTH // 4
player_y = HEIGHT - player_height - 50
player_vel_y = 0
gravity = 1
jump_height = -15

# Obstacles
obstacle_width, obstacle_height = 50, 50
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 50
obstacle_vel = 5

# Score
score = 0
font = pygame.font.SysFont("comicsans", 30)

def draw_player(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, player_width, player_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, (x, y, obstacle_width, obstacle_height))

def check_collision(player_x, player_y, obstacle_x, obstacle_y):
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    return player_rect.colliderect(obstacle_rect)

def main():
    global player_y, player_vel_y, obstacle_x, score

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_y == HEIGHT - player_height - 50:
                    player_vel_y = jump_height

        # Update player position
        player_vel_y += gravity
        player_y += player_vel_y
        if player_y >= HEIGHT - player_height - 50:
            player_y = HEIGHT - player_height - 50
            player_vel_y = 0

        # Update obstacle position
        obstacle_x -= obstacle_vel
        if obstacle_x + obstacle_width < 0:
            obstacle_x = WIDTH
            score += 1

        # Check for collision
        if check_collision(player_x, player_y, obstacle_x, obstacle_y):
            print(f"Game Over! Score: {score}")
            running = False

        # Draw everything
        screen.fill(WHITE)
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        # Display score
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()