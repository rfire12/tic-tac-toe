import pygame


class Square:
    def __init__(self, window, position):
        self.__window = window
        self.__position = position
        self.__square = pygame.draw.rect(window, (194, 194, 194), position)
        self.__marked_by = False

    def get_square(self):
        return self.__square

    def mark(self, player):
        if not self.__marked_by:
            color = (50, 168, 82) if player == 1 else (252, 3, 3)
            self.__square = pygame.draw.rect(self.__window, color, self.__position)
            self.__marked_by = player

    def get_marked_by(self):
        return self.__marked_by
