import pygame
import square


class Board:
    __winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                           [0, 3, 6], [1, 4, 7], [2, 5, 8],
                           [0, 4, 8], [2, 4, 6]]

    def __init__(self, window, player):
        self.__board = [square.Square(window, (25, 55, 150, 150)), square.Square(window, (200, 55, 150, 150)),
                        square.Square(window, (375, 55, 150, 150)), square.Square(window, (25, 230, 150, 150)),
                        square.Square(window, (200, 230, 150, 150)), square.Square(window, (375, 230, 150, 150)),
                        square.Square(window, (25, 405, 150, 150)), square.Square(window, (200, 405, 150, 150)),
                        square.Square(window, (375, 405, 150, 150))]
        self.__player = player
        self.__window = window

    def mark_square(self, current_player, position):
        marked_valid_pos = False
        for square_box in self.__board:
            if square_box.get_square().collidepoint(position) and square_box.get_marked_by() is False:
                square_box.mark(current_player)
                marked_valid_pos = True

        return marked_valid_pos

    def check_winning_positions(self, current_player):
        for win_position in self.__winning_positions:
            first_square = self.__board[win_position[0]].get_marked_by() == current_player
            second_square = self.__board[win_position[1]].get_marked_by() == current_player
            third_square = self.__board[win_position[2]].get_marked_by() == current_player

            if first_square and second_square and third_square:
                # Render win message
                message_render = pygame.font.Font(pygame.font.get_default_font(), 36)
                text_surface = message_render.render(f'Player {current_player} wins', True, (255, 255, 255))

                self.__window.blit(text_surface, (150, 250))

    def get_player(self):
        return self.__player

