import pygame


class Square:
    def __init__(self, window, position):
        self.__square = pygame.draw.rect(window, (194, 194, 194), position)
