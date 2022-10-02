import socket


class Server:

    def __init__(self, address, port):
        self.address = address
        self.port = port

    def run_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем сервер на IP/TCP
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # При перезапуске сервера не ждем времени на получение пакетов
        self.server.bind((self.address, self.port))  # Подключаемся к адресу
        self.server.listen(2)  # И начинаем слушать два подключения
        print(f'Server with address "{self.address}" and port "{self.port}" is running and waiting for connecting')

        while True:
            self.client, self.client_addr = self.server.accept()
            print(f'Client "{self.client_addr}" connected to server')

            self.data = self.client.recv(1024).decode('utf-8')  # Получаем от клиента инфу
            if not self.data:
                break
            self.answer = f'Thanks for sending us next data : {self.data}'
            self.client.send(self.answer.encode('utf-8'))
            print(f'Got "{self.data}" from client and send answer to him')
        self.server.close()


if __name__ == '__main__':
    server = Server("", 5555)
    server.run_server()
