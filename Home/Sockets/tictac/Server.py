import json
import socket
import threading


class TicTacToeServer:
    def __init__(self, host="127.0.0.1", port=65432):
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(2)
        print(f"Server listening on {host}:{port}")

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # рядки
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # колонки
            (0, 4, 8), (2, 4, 6)  # діагоналі
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != " ":
                return self.board[combo[0]]

        return None

    def handle_client(self, conn, player):
        while True:
            if player == self.current_player:
                data = conn.recv(1024).decode().strip()
                if data.isdigit() and 0 <= int(data) < 9 and self.board[int(data)] == " ":
                    self.board[int(data)] = player
                    winner = self.check_winner()
                    if winner:
                        self.send_board()
                        for conn in self.connections:
                            conn.sendall(json.dumps(f"WINNER:{winner}").encode())
                            return
                    self.current_player = "O" if player == "X" else "X"
                    self.send_board()

    def send_board(self):
        for conn in self.connections:
            conn.sendall(json.dumps(self.board).encode() + "\n".encode())

    def start(self):
        self.connections = []
        for i in range(2):
            conn, addr = self.sock.accept()
            self.connections.append(conn)
            threading.Thread(target=self.handle_client, args=(conn, "X" if i == 0 else "O")).start()


server = TicTacToeServer()
server.start()
