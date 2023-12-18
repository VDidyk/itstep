# Створіть два окремих "мікросервіси" (дві окремі
# програми). Одна програма створює та експортує дані у
# форматі JSON, а інша програма завантажує та обробляє ці
# дані. Це може бути, наприклад, система, яка створює та
# обробляє замовлення.

import socket
import threading


def client_handler(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)

            for client in clients:
                if client is not client_socket:
                    client.send(message)
        except ConnectionResetError:
            clients.remove(client_socket)
            client_socket.close()
            break


host = '127.0.0.1'
port = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

print(f"Server is listening on {host}:{port}")

try:
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()
except KeyboardInterrupt:
    print("Server is shutting down.")
finally:
    server.close()
