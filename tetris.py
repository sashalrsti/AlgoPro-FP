import pygame
import sys
from game import Game
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Walmart Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Variables to track key states
moving_left = False
moving_right = False
moving_down = False

# Timers for movement
down_movement_timer = 0
down_movement_interval = 100  # Time in milliseconds

left_movement_timer = 0
left_movement_interval = 100  # Time in milliseconds

right_movement_timer = 0
right_movement_interval = 100  # Time in milliseconds

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT:
                moving_left = True
                left_movement_timer = left_movement_interval  # Reset timer
            if event.key == pygame.K_RIGHT:
                moving_right = True
                right_movement_timer = right_movement_interval  # Reset timer
            if event.key == pygame.K_DOWN:
                moving_down = True
                if game.k_down_flag == False:
                    game.update_score(0, 1)
                    game.k_down_flag = True
                down_movement_timer = down_movement_interval  # Reset timer
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_DOWN:
                moving_down = False
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()

    # Handle continuous movement
    if not game.game_over:
        # Handle left movement with timer
        if moving_left:
            left_movement_timer -= clock.get_time()  # Decrease timer by elapsed time
            if left_movement_timer <= 0:
                game.move_left()
                left_movement_timer = left_movement_interval  # Reset timer

        # Handle right movement with timer
        if moving_right:
            right_movement_timer -= clock.get_time()  # Decrease timer by elapsed time
            if right_movement_timer <= 0:
                game.move_right()
                right_movement_timer = right_movement_interval  # Reset timer

        # Handle down movement with timer
        if moving_down:
            down_movement_timer -= clock.get_time()  # Decrease timer by elapsed time
            if down_movement_timer <= 0:
                game.move_down()
                down_movement_timer = down_movement_interval  # Reset timer

    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))

    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(center=(score_rect.centerx, score_rect.centery)))
    game.draw(screen)

    pygame.display.update()
    clock.tick(60)