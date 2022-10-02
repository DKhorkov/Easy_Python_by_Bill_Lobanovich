import socket
from datetime import datetime
import pickle


class Server:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(('', 5000))
        self.server.listen()

    def run_server(self):
        print('Server is waiting for connection')
        self.conn, self.addr = self.server.accept()
        print(f'user with add {self.addr} connected to the server')
        while True:

            self.data = self.conn.recv(4096).decode('utf-8')
            print(f'Next data was received from client: {self.data}')

            if not self.data:
                break

            if self.data == 'time':
                self.message = pickle.dumps(datetime.now())
            else:
                self.message = pickle.dumps('Unknown command')
            self.conn.send(self.message)
            print('data was sent')
        self.server.close()


if __name__ == '__main__':
    server = Server()
    server.run_server()
