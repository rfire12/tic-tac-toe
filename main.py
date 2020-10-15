import pygame

pygame.init()
window = pygame.display.set_mode((550, 550))
pygame.display.set_caption('Tic Tac Toe')
game_running = True

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

pygame.quit();