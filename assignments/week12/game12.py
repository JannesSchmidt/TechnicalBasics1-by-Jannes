import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

# defining colors to safe time later
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# implementing surface
player_surf = pygame.Surface((40, 40))
player_surf.fill(WHITE)
player_rect = player_surf.get_rect(center=(WIDTH//2, HEIGHT - 50))

blocks = []
for _ in range(5):
    rect = pygame.Rect(random.randint(0, WIDTH - 30), random.randint(-600, -50), 30, 30)
    blocks.append(rect)

score = 0
font = pygame.font.SysFont("arial", 32)

# Shows instructions at the beginning
win.fill(BLACK)
instruction_text = font.render("Use Arrow Keys to Move. Avoid Red Blocks!", True, WHITE)
win.blit(instruction_text, (100, HEIGHT//2))
pygame.display.flip()
pygame.time.delay(2000)

running = True
while running:
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() # movement commands
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5

    player_rect.clamp_ip(win.get_rect())

    for block in blocks: # "Enemies" or Obstacles rather
        block.y += 5
        pygame.draw.rect(win, RED, block)
        if block.y > HEIGHT:
            block.x = random.randint(0, WIDTH - 30)
            block.y = random.randint(-100, -50)
            score += 1
        if player_rect.colliderect(block): # Game over condition
            text = font.render("Game Over", True, RED)
            win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            running = False

    if score >= 100: # Winning condtion
        text = font.render("You won!", True, WHITE)
        win.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False

    win.blit(player_surf, player_rect)
    score_surf = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_surf, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

# note to self, adding this in the final assignment