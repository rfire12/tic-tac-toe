import pygame
import square
import board
import ast
import time

import socket
import threading

# Setup
pygame.init()
window = pygame.display.set_mode((550, 580))
pygame.display.set_caption('Tic Tac Toe')
player_board = board.Board(window, 1)




game_running = True
current_player = 1

# TCP CONNECTION
HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


def render_title(player):
    color = 'Green' if player == 1 else 'Red'
    message_render = pygame.font.Font(pygame.font.get_default_font(), 20)
    text_surface = message_render.render(f'You are Player {str(player)} - Color: {color}', True, (255, 255, 255))
    window.blit(text_surface, (125, 15))


def create_thread(target):
    thread = threading.Thread(None, target)
    thread.daemon = True
    thread.start()


def receive_data():
    global position, current_player, player_board

    while True:
        time.sleep(1)
        recv_data = sock.recv(1024).decode()

        # It's only executed the first time a connection is established.
        if 'player' in recv_data:
            player_number = int(recv_data.split('=')[1])

            player_board = board.Board(window, player_number)  # Initialize Board
            render_title(player_number)
        else:
            position = eval(recv_data)  # Cast
            if recv_data and player_board.get_player() != current_player:  # If it is receiving data from opponent
                player_board.mark_square(current_player, position)  # Mark marked position by opponent in the receiving client board
                player_board.check_winning_positions(current_player) # Check if the opponent won in order to display a winning message
            current_player = 1 if current_player == 2 else 2  # switch players


create_thread(receive_data)


while game_running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        # If clicked and it's player turn
        if event.type == pygame.MOUSEBUTTONUP and current_player == player_board.get_player():
            position = pygame.mouse.get_pos()

            if player_board.mark_square(current_player, position):
                player_board.check_winning_positions(current_player)
                sock.sendall(str(position).encode())
    pygame.display.update()

pygame.quit()

