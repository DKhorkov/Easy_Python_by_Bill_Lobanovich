import os
import socket
import threading


class Client:

    def __init__(self, server_addr, port):
        self.server_addr = server_addr
        self.server_port = port

    def thread_for_listen_for_messages(self, client):
        while True:
            self.message = client.recv(4096).decode('utf-8')
            print(f"\r\r{self.message}\nMe: ", end='')

    def connect_to_server(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Создаем клиента на IP/TCP
        self.client.connect((self.server_addr, self.server_port))
        self.client.send('__join_server'.encode('utf-8'))
        threading.Thread(target=self.thread_for_listen_for_messages, args=(self.client,)).start()
        while True:
            self.data = input('Me: ')
            if self.data.lower() == 'q':
                break
            self.client.send(self.data.encode('utf-8'))
        self.client.close()


if __name__ == '__main__':
    os.system('clear')  # Очищаем консоль перед чатом
    client = Client("", 5555)
    client.connect_to_server()
    