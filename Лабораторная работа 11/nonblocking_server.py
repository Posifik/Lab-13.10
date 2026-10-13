import socket
import os
import time

PORT = 9995

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("127.0.0.1", PORT))
server_socket.listen(1)
server_socket.setblocking(False)

print(f"[СЕРВЕР] Неблокирующий режим. PID: {os.getpid()}")
print("[СЕРВЕР] Ожидаем подключение (Polling)...")

client_socket = None

while True:
    try:
        client_socket, client_address = server_socket.accept()
        print(f"\n[СЕРВЕР] Подключение от {client_address}")
        break
    except BlockingIOError:
        print(".", end="", flush=True)
        time.sleep(0.01)

client_socket.setblocking(False)
print("[СЕРВЕР] Ожидаем данные...")

while True:
    try:
        data = client_socket.recv(1024)

        if data:
            print(f"\n[СЕРВЕР] Получено: {data.decode('utf-8')}")
            break

        # Пустой результат recv означает, что клиент закрыл
        # свою сторону соединения без новых данных.
        print("\n[СЕРВЕР] Клиент закрыл соединение.")
        break

    except BlockingIOError:
        print("*", end="", flush=True)
        #time.sleep(0.01)

client_socket.close()
server_socket.close()
print("[СЕРВЕР] Работа завершена.")
