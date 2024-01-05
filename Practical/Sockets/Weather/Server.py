import socket
import threading
import requests


def get_weather(city_name):
    api_key = '58a5f09340cc87dcd0952ecd5c078cfd'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data['cod'] == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp'] - 273.15
        return f"Weather: {weather}, Temperature: {temperature:.2f}°C"
    else:
        return "Weather data not available."


def load_weather_data(file_path):
    weather_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) == 3:
                country, city, weather = parts
                weather_data[(country, city)] = weather
    return weather_data


def handle_client(conn, weather_data):
    try:
        data = conn.recv(1024).decode()
        country, city = data.split(',')
        weather = get_weather(city)
        conn.sendall(weather.encode())
    finally:
        conn.close()


def start_server(host, port, weather_data):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server running on {host}:{port}")

    try:
        while True:
            conn, addr = server_socket.accept()
            threading.Thread(target=handle_client, args=(conn, weather_data)).start()
    finally:
        server_socket.close()


weather_data = load_weather_data('data.txt')
start_server('localhost', 12345, weather_data)
