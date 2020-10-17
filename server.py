import socket
import threading
import time

# TCP CONNECTION
HOST = '127.0.0.1'
PORT = 65432
connection_established = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()
ThreadCount = 0
connections = []


def receive_data(conn):
    global connections
    while True:
        time.sleep(1)
        click_position = conn.recv(1024)

        for conn_element in connections:
            conn_element.send(click_position)


def create_thread(target, conn):
    thread = threading.Thread(group=None, target=target, args=(conn,))
    thread.daemon = True
    thread.start()


while True:
    connection, address = sock.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    connections.append(connection)

    player_number = '1' if ThreadCount == 0 else '2'
    player_number = 'player=' + player_number
    connection.send(player_number.encode())

    create_thread(receive_data, connection)
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
sock.close()
