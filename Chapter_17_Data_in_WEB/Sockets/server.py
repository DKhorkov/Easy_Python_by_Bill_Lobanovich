import socket


class Server:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.clients = []

    def create_server(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем сервер на IP/UDP
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                               1)  # При перезапуске сервера не ждем времени на получение пакетов
        self.server.bind((self.address, self.port))  # Подключаемся к адресу
        print(f'Server with address "{self.address}" and port "{self.port}" is running and waiting for connecting')

    def check_client_on_existence(self, client_addr):
        if client_addr not in self.clients:
            self.clients.append(client_addr)
            print(self.clients)

    def send_client_message_to_others(self):
        self.answer = f"Client{self.client_id}: {self.message.decode('utf-8')}"
        for client in self.clients:
            if self.client_addr == client:
                continue
            self.server.sendto(self.answer.encode('utf-8'), client)

    def run_server(self):
        self.create_server()
        while True:
            self.message, self.client_addr = self.server.recvfrom(4096)
            self.check_client_on_existence(self.client_addr)

            if not self.message:
                continue

            self.client_id = self.client_addr[1]
            if self.message.decode('utf-8') == '__join_server':
                print(f'Client{self.client_id} has joined the chat!')
                continue

            self.send_client_message_to_others()
        self.server.close()


if __name__ == '__main__':
    server = Server("", 5555)
    server.run_server()
