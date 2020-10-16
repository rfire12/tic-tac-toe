import pygame
import square

pygame.init()
window = pygame.display.set_mode((550, 550))
pygame.display.set_caption('Tic Tac Toe')
game_running = True
board = [square.Square(window, (25, 25, 150, 150)), square.Square(window, (200, 25, 150, 150)),
         square.Square(window, (375, 25, 150, 150)), square.Square(window, (25, 200, 150, 150)),
         square.Square(window, (200, 200, 150, 150)), square.Square(window, (375, 200, 150, 150)),
         square.Square(window, (25, 375, 150, 150)), square.Square(window, (200, 375, 150, 150)),
         square.Square(window, (375, 375, 150, 150))]

while game_running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    pygame.display.update()
pygame.quit()






