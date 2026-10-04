"""Организация потока ввода-вывода
Клиент-сервер (СЕРВЕР)"""
import socket

# Параметры сервера
ip = '127.0.0.1'
port = 9001
endpoint = (ip, port)
# Сокет сервера
#                        Adress Family    Потоковый сокет
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(endpoint)
server.listen(10) # В асинхр режиме может обсл 10 чел

# Режим ожидания запросов
print(f'Сервер запущен на IP:{ip} Порт:{port}')
print('Ожидание запросов...')
#обесп получ запросов, адрес, откуда придет запрос
connection, address = server.accept()
# Обмен данными с клиентом
try:
    print(f'Установлено соединение с клиентом {address}')
    while True:
        client_message = connection.recv(1024).decode('utf-8')
        # приним сообщение по байту, декодим
        if client_message == 'stop_server' or not client_message:
            break
        print(f'Запрос: [{client_message}]')
        # отправляем сообщение клиенту
        server_message = input('Сообщение клиенту: ')
        connection.send(server_message.encode('utf-8'))
        print('Сообщение отправлено')
except BaseException as error:
    print(error)
finally:
    connection.close()
    print('Сервер остановлен')

