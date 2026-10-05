from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
from time import strftime, localtime

host = gethostbyname('localhost')
port = 9090
clients = []

server = socket(AF_INET, SOCK_DGRAM)
server.bind((host, port)) # вставляем кортежи

_exit = False
print('Server started on', host, 'port', port)
while not _exit:
    try:
        data, addr = server.recvfrom(1024)
        if not addr in clients:
            clients.append(addr)
        set_time = strftime("%d.%m.%Y %X", localtime())
        print(f'{addr[0]} : {addr[1]} - {set_time}')
        print(f'{data.decode('utf-8')}')
        for client in clients:
            if client != addr:
                server.sendto(data, client)
    except RuntimeError:
        print('Server disconnected')

server.close()