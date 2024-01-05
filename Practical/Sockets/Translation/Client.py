import socket

def get_translation(server_host, server_port, text, lang):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_host, server_port))
        s.sendall(f"{text};{lang}".encode())
        translated_text = s.recv(1024).decode()
        print(f"Translated Text: {translated_text}")


while True:
    get_translation('localhost', 12345, input("Enter the text: "), 'uk')  # Translating to Spanish
