import socket
from googletrans import Translator, LANGUAGES

def translate_text(text, dest_lang):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=dest_lang)
        return translation.text
    except Exception as e:
        return f"Error in translation: {e}"

def handle_client(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        text, lang = data.split(';')
        translated_text = translate_text(text, lang)
        conn.sendall(translated_text.encode())
    conn.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Translation server running on {host}:{port}")

    while True:
        conn, _ = server_socket.accept()
        handle_client(conn)

start_server('localhost', 12345)
