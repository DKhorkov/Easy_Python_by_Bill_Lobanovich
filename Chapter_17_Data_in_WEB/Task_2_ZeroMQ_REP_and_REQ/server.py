import datetime

import zmq


class Server:

    def __init__(self):
        self.context = zmq.Context()
        self.server = self.context.socket(zmq.REP)
        self.server.bind('tcp://{}:{}'.format('127.0.0.1', 5555))  # Тут прямо обязательно передать айпи строкой

    def run_server(self):
        print('Server is running')
        while True:
            print('Waiting for data')
            self.data = self.server.recv().decode('utf-8')
            print(f'Received data: {self.data}')

            if self.data == "time":
                self.answer = str(datetime.datetime.utcnow())
            else:
                self.answer = 'Unknown command'

            self.server.send(self.answer.encode('utf-8'))
            print('Answer was sent')


if __name__ == '__main__':
    server = Server()
    server.run_server()
