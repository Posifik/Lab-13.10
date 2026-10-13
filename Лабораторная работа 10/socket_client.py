import socket
import time

PORT = 9999

print("[КЛИЕНТ] Создаем сокет...")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[КЛИЕНТ] Пауза 3 секунды перед подключением...")
time.sleep(3)

print("[КЛИЕНТ] Подключаемся к серверу...")
client_socket.connect(("127.0.0.1", PORT))

print("[КЛИЕНТ] Соединение установлено.")
print("[КЛИЕНТ] Пауза 3 секунды перед отправкой...")
time.sleep(3)

client_socket.sendall("Test payload".encode("utf-8"))
print("[КЛИЕНТ] Данные отправлены.")

client_socket.close()
print("[КЛИЕНТ] Сокет закрыт.")
