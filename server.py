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


def hold_connection():
    global connection, address, sock
    connection, address = sock.accept()
    connections.append(connection)
    print('New connection')
    receive_data()

# create_thread(hold_connection)


while True:
    connection, address = sock.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    connections.append(connection)
    create_thread(receive_data, connection)
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
sock.close()
