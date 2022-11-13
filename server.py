import socket
import threading
import time

PORT = 5050
HEADER = 64
FORMAT = 'utf-8'
DISCONNET_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
# Here we are getting local ip address of host/server
ADDR = (SERVER, PORT)
print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# with the babove method we are creating a socket for establishing connection
# AF_INET refers to address-family IPV4
# SOCK_STREAM refres to connection-oriented TCP Protocol
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNET_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()


def start():
    server.listen()
    print(f"[Listening] Server is listening on {SERVER} ")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()}")


print("[Starting] server is starting ......")
start()
