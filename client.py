import pygame
import square
import board
import ast
import time

import socket
import threading

# Setup
pygame.init()
window = pygame.display.set_mode((550, 550))
pygame.display.set_caption('Tic Tac Toe')
player_board = board.Board(window, 1)
game_running = True
current_player = 1

# TCP CONNECTION
HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


def create_thread(target):
    thread = threading.Thread(None, target)
    thread.daemon = True
    thread.start()


def receive_data():
    global position, current_player
    while True:
        time.sleep(1)
        recv_data = sock.recv(1024).decode()
        position = eval(recv_data)  # Cast
        if recv_data:
            player_board.mark_square(current_player, position)
            player_board.check_winning_positions(current_player)
            current_player = 1 if current_player == 2 else 2  # switch players


create_thread(receive_data)


while game_running:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()

            if player_board.mark_square(current_player, position):
                player_board.check_winning_positions(current_player)
                sock.sendall(str(position).encode())
    pygame.display.update()

pygame.quit()

