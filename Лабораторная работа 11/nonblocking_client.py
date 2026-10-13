
import socket
import time

PORT = 9995

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[КЛИЕНТ] Ждём 3 секунды перед подключением...")
time.sleep(3)

client_socket.connect(("127.0.0.1", PORT))
print("[КЛИЕНТ] Подключено. Ждём перед отправкой...")
time.sleep(3)

client_socket.sendall("Hello from non-blocking test".encode("utf-8"))
print("[КЛИЕНТ] Данные отправлены.")

client_socket.close()
print("[КЛИЕНТ] Сокет закрыт.")
