import pygame
import random

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
BACKGROUND_COLOR = (255, 255, 255)
NUM_CATS = random.randint(1, 100)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Animated Cat')
clock = pygame.time.Clock()

# Load and scale image
base_image = pygame.image.load("cat.png").convert_alpha()
base_image = pygame.transform.scale(base_image, (250, 250))

class Cat:
    def __init__(self):
        self.image = base_image.copy()
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.dx = random.randint(-2, 2)
        self.dy = random.randint(-2, 2)
        # Make sure the cat moves
        if self.dx == 0:
            self.dx = 1
        if self.dy == 0:
            self.dy = 1

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Reset if cat leaves screen (Improved by AI)
        if self.x < -100 or self.x > SCREEN_WIDTH + 100 or self.y < -100 or self.y > SCREEN_HEIGHT + 100:
            self.x = SCREEN_WIDTH // 2
            self.y = SCREEN_HEIGHT // 2
            self.dx = random.randint(-2, 2)
            self.dy = random.randint(-2, 2)
            if self.dx == 0:
                self.dx = 1
            if self.dy == 0:
                self.dy = 1

        screen.blit(self.image, (self.x, self.y))

# Create multiple cat instances
cats = [Cat() for _ in range(NUM_CATS)]

# Main loop
running = True
while running:
    clock.tick(69)
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for cat in cats:
        cat.update()

    pygame.display.flip()

pygame.quit()
