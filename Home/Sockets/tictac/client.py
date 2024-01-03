import json
import tkinter as tk
import tkinter.messagebox
import socket
from threading import Thread


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()

    def create_buttons(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.window, text='', font='normal 20 bold', width=5, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_click(self, row, col):
        connection.send(row * 3 + col)

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def check_draw(self):
        return all(self.buttons[row][col]["text"] != "" for row in range(3) for col in range(3))

    def start(self):
        self.window.mainloop()


class Connection:
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 65432
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()

    def read(self):
        while True:
            try:
                data = self.s.recv(1024)
                if not data:
                    break

                response = data.decode()

                if response.startswith('"WINNER'):
                    winner = response.replace('"', '').split(':')[1].strip()
                    self.handle_winner(winner)
                    break
                elif response == '"DRAW':
                    self.handle_draw()
                    break
                else:
                    self.update_desk(json.loads(response))
            except socket.error as e:
                print(f"Socket error: {e}")
                break

    def handle_winner(self, winner):
        tk.messagebox.showinfo("Game Over", f"Player {winner} wins!")
        self.close_connection()

    def handle_draw(self):
        tk.messagebox.showinfo("Game Over", "It's a draw!")
        self.close_connection()

    def close_connection(self):
        self.s.close()
        game.window.quit()

    def update_desk(self, data):
        count = 0
        for i in data:
            btn = game.buttons[count // 3][count % 3]
            btn.config(text=i)
            count += 1

    def send(self, i):
        move = json.dumps(i)
        self.s.sendall(move.encode())

    def connect(self):
        try:
            self.s.connect((self.ip, self.port))
            t1 = Thread(target=self.read)
            t1.start()
        except socket.error as e:
            print(f"Connection error: {e}")


connection = Connection()

game = TicTacToe()
game.start()
