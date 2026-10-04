"""Организация потока ввода-вывода
Клиент-сервер (КЛИЕНТ)"""
import socket

# Параметры сервера
ip = '127.0.0.1'
port = 9001
endpoint = (ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(endpoint)
    while True:
        client_message = input('Запрос серверу: ')
        client.send(client_message.encode('utf-8'))
        if client_message == 'stop_server' or not client_message:
            break
        # примем сообщения от сервера
        server_message = client.recv(1024).decode('utf-8')
        print(f'Ответ сервера: [{server_message}]')

        _continue = input('Продолжать обмен (y/n)?: ')
        if _continue == 'n':
            break
except BaseException as error:
    print(error)
finally:
    client.close()
    print('Сервер остановлен')
