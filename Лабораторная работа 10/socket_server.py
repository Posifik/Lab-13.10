
import socket
import os

PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Для первого эксперимента SO_REUSEADDR выключен:
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print(f"[СЕРВЕР] Инициализация. PID: {os.getpid()}")

server_socket.bind(("127.0.0.1", PORT))
server_socket.listen(1)

print(f"[СЕРВЕР] Сокет слушает порт {PORT}.")
print("[СЕРВЕР] Ожидание подключения: accept()...")

client_socket, client_address = server_socket.accept()

print(f"[СЕРВЕР] Подключение от {client_address}")
print("[СЕРВЕР] Ожидание данных: recv()...")

data = client_socket.recv(1024)

print(f"[СЕРВЕР] Получено: {data.decode('utf-8')}")

print("[СЕРВЕР] Закрываем соединение.")
client_socket.close()
server_socket.close()
