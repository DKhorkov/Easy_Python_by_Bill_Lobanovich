import socket


class Client:

    def __init__(self, server_addr, port):
        self.server_addr = server_addr
        self.server_port = port

    def connect_to_server(self):
        while True:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем клиента на IP/TCP
            self.client.connect((self.server_addr, self.server_port))

            self.data = input('Enter data to send it to server: ')
            if self.data.lower() == 'q':
                break
            self.client.sendall(self.data.encode())
            self.answer = self.client.recv(1024).decode('utf-8')
            print(f'Server provided us with an answer: {self.answer}')
        self.client.close()


if __name__ == '__main__':
    client = Client("", 5555)
    client.connect_to_server()