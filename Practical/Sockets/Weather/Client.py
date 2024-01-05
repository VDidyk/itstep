import socket

def get_weather(host, port, country, city):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(f"{country},{city}".encode())
        weather = s.recv(1024).decode()
        print(f"Weather in {city}, {country}: {weather}")

while True:
    get_weather('localhost', 12345, input("Enter the country: "), input("Enter the city: "))
