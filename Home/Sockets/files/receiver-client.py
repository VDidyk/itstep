import socket
import threading
from datetime import datetime
import json


def receive_message(client_socket):
    while True:
        try:
            message = json.loads(client_socket.recv(1024).decode('utf-8'))
            print(f"{datetime.now().strftime('%d.%m.%Y %I:%M:%S')} {message['user']}: {message['message']}")
        except ConnectionResetError:
            print("Connection lost to server.")
            break
        except OSError:
            break


host = '127.0.0.1'
port = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

receive_message(client)
