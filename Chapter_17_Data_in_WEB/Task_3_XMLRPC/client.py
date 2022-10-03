from xmlrpc.client import ServerProxy


class Client:

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port

    def main(self):
        print('Connected to server.\nPrint "time" to know current time or "quit" to exit program')
        self.connection = ServerProxy(f'http://{self.addr}:{self.port}')
        while True:
            self.command = input('Enter command: ')
            if self.command == 'quit':
                break
            elif self.command == 'time':
                self.answer = self.connection.current_time()
            else:
                self.answer = self.connection.unknown_command()
            print(self.answer)


if __name__ == '__main__':
    client = Client('localhost', 5001)
    client.main()