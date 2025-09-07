import pygame
import random
import os


pygame.init()

# Defines colors
WIDTH, HEIGHT = 1280, 720
FPS = 60
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Creates the display window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Retro Comet Dodger")
clock = pygame.time.Clock()

# Sets up the font
font = pygame.font.Font(None, 36)


def load_image(filename, size=None, rotate=0):
    base_path = os.path.dirname(__file__)
    image_path = os.path.join(base_path, filename)


    image = pygame.image.load(image_path).convert_alpha()
    if size:
        image = pygame.transform.scale(image, size)
    if rotate != 0:
        image = pygame.transform.rotate(image, rotate)
    return image


def main_game():
    # Loads and scales the player image
    player_image = load_image('ship.png', size=(60, 60))

    # Positions the player's rectangle
    player = player_image.get_rect(center=(WIDTH // 2, HEIGHT - 60))

    # Loads and rotates the comet image
    comet_image = load_image('Comet.png', size=(30, 30), rotate=-45)

    # Creates comet rectangles
    blocks = [pygame.Rect(random.randint(0, WIDTH - 40), random.randint(-600, -50), 40, 40) for _ in range(5)]
    retro_score = 0
    running = True
    speed = 5
    difficulty_level = 0


    # Loads and scales the background image
    background_image = load_image('retro bg.jpg', size=(WIDTH, HEIGHT))
    background_image.set_alpha(50) 
    # I don't know why - I wanted to make the background a bit see through because I found it hard to look at...
    # And now there is this cool trail effect. xD


    # Game variables
    start_time = pygame.time.get_ticks()
    countdown_duration = 5
    show_instructions = True
    game_over = False

    while running:
        win.blit(background_image, (0, 0))

        # Handles quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

            # Handles button clicks in the game over state
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                if main_menu_button.collidepoint(event.pos):
                    main_game()
                    return

        # Creates countdown and instruction logic
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - start_time) / 1000
        remaining_time = countdown_duration - int(elapsed_time)

        if show_instructions:
            # Displays instructions
            instructions_text = [
                "Controls: Use the arrow keys to move.",
                "Goal: Avoid the comets.",
                "Try to reach 200 points!",
                f"Starting in: {remaining_time}"
            ]
            for i, line in enumerate(instructions_text):
                instruction_surf = font.render(line, True, WHITE)
                instruction_rect = instruction_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 60 + i * 40))
                win.blit(instruction_surf, instruction_rect)

            if remaining_time <= 0:
                show_instructions = False

        elif not game_over:
            # Handles game controls
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: player.x -= 5
            if keys[pygame.K_RIGHT]: player.x += 5
            if keys[pygame.K_UP]: player.y -= 5
            if keys[pygame.K_DOWN]: player.y += 5
            player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

            for block in blocks:
                block.y += speed
                if player.colliderect(block):
                    game_over = True
                    break

                if block.y > HEIGHT:
                    block.y = random.randint(-100, -50)
                    block.x = random.randint(0, WIDTH - 40)
                    retro_score += 1

            # Checks for win condition
            if retro_score >= 200:
                game_over = True

            # Increases difficulty level every 10 points
            new_difficulty_level = retro_score // 10
            if new_difficulty_level > difficulty_level:
                difficulty_level = new_difficulty_level
                speed += 0.25
                blocks.append(
                    pygame.Rect(random.randint(0, WIDTH - 40), random.randint(-600, -50), 40, 40))

            # Draws the player image and comets
            win.blit(player_image, player)
            for block in blocks:
                win.blit(comet_image, block)

            score_surf = font.render(f"Score: {retro_score} / 200", True, WHITE)
            win.blit(score_surf, (10, 10))

        else:
            # Displays victory or defeat text
            final_text = "Victory!" if retro_score >= 200 else "Game Over!"
            final_color = GREEN if retro_score >= 200 else (255, 0, 0)

            final_font = pygame.font.Font(None, 80)
            final_text_surf = final_font.render(final_text, True, final_color)
            final_text_rect = final_text_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
            win.blit(final_text_surf, final_text_rect)

            # Draws the "Play Again" button
            main_menu_text_surf = font.render("Play Again", True, WHITE)
            main_menu_button = main_menu_text_surf.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))
            pygame.draw.rect(win, GRAY, main_menu_button.inflate(20, 10))
            win.blit(main_menu_text_surf, main_menu_button)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main_game()
