import zmq


class Client:

    def __init__(self):
        self.context = zmq.Context()
        self.client = self.context.socket(zmq.REQ)
        self.client.connect('tcp://{}:{}'.format("127.0.0.1", 5555))

    def connect_to_server(self):
        print('Connected to server.\nPrint "time" to know current time or "quit" to exit program')
        while True:
            self.command = input("U'r input: ").encode('utf-8')
            self.client.send(self.command)
            print('Command was sent')

            self.answer = self.client.recv().decode('utf-8')
            print(self.answer)


if __name__ == '__main__':
    client = Client()
    client.connect_to_server()
