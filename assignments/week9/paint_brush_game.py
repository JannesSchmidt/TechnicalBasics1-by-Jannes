import pygame
import random

# Initialize Pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tiny Circle Drawing Game")
font_small = pygame.font.SysFont(None, 24)

# Brush class
class Brush:
    def __init__(self, color=(0, 0, 0), size=5):
        self._color = color
        self._size = size

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def set_size(self, size):
        self._size = size

    def get_size(self):
        return self._size

    def draw(self, pos):
        pygame.draw.circle(screen, self._color, pos, self._size)

# Subclass Brush
class CircleBrush(Brush):
    def __init__(self, color=(0, 0, 0), size=5):
        super().__init__(color, size)

    def randomize_color(self):
        self.set_color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

# Setup
clock = pygame.time.Clock()
brush = CircleBrush()
drawing = False
strokes = []

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))

    # Drawing
    for color, size, pos in strokes:
        pygame.draw.circle(screen, color, pos, size)

    # QUitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse commands
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            drawing = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            drawing = False

        # Keyboard commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                strokes.clear()
            elif event.key == pygame.K_UP:
                brush.set_size(min(brush.get_size() + 1, 30))
            elif event.key == pygame.K_DOWN:
                brush.set_size(max(1, brush.get_size() - 1))
            elif event.key == pygame.K_SPACE:
                brush.randomize_color()

    # Drawing
    if drawing:
        pos = pygame.mouse.get_pos()
        brush.draw(pos)
        strokes.append((brush.get_color(), brush.get_size(), pos))

    # Help Text AI-Generated
    help_text = [
        "Draw: Hold left mouse button",
        "Change color: Spacebar",
        "Brush size: ↑ / ↓",
        "Clear: C"]
    for i, line in enumerate(help_text):
        text_surf = font_small.render(line, True, (50, 50, 50))
        screen.blit(text_surf, (10, SCREEN_HEIGHT - (len(help_text) - i) * 20 - 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# The command explanation is included in the running code or in line 90-93 ^-^