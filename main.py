import pygame
import square

# Setup
pygame.init()
window = pygame.display.set_mode((550, 550))
pygame.display.set_caption('Tic Tac Toe')
game_running = True
message_render = pygame.font.Font(pygame.font.get_default_font(), 36)

# Game details
board = [square.Square(window, (25, 25, 150, 150)), square.Square(window, (200, 25, 150, 150)),
         square.Square(window, (375, 25, 150, 150)), square.Square(window, (25, 200, 150, 150)),
         square.Square(window, (200, 200, 150, 150)), square.Square(window, (375, 200, 150, 150)),
         square.Square(window, (25, 375, 150, 150)), square.Square(window, (200, 375, 150, 150)),
         square.Square(window, (375, 375, 150, 150))]

winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],
                     [0, 4, 8], [2, 4, 6]]

current_player = 1


def mark_square():
    marked_valid_pos = False
    for square_box in board:
        if square_box.get_square().collidepoint(pos) and square_box.get_marked_by() is False:
            square_box.mark(current_player)
            marked_valid_pos = True

    return marked_valid_pos


def check_winning_positions():
    for win_position in winning_positions:
        first_square = board[win_position[0]].get_marked_by() == current_player
        second_square = board[win_position[1]].get_marked_by() == current_player
        third_square = board[win_position[2]].get_marked_by() == current_player

        if first_square and second_square and third_square:
            text_surface = message_render.render(f'Player {current_player} wins', True, (255, 255, 255))
            window.blit(text_surface, (150, 250))


while game_running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if mark_square():
                check_winning_positions()
                current_player = 1 if current_player == 2 else 2  # switch players

    pygame.display.update()




pygame.quit()






