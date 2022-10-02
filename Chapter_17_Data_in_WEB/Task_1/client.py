import socket
import pickle


class Client:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("", 5000))

    def connect_to_server(self):
        print('Print "time" to know current time or "quit" to exit program')
        while True:
            self.command = input("U'r input: ")
            if self.command == 'quit':
                break

            self.client.send(self.command.encode('utf-8'))
            self.answer_from_server = pickle.loads(self.client.recv(4096))
            print(self.answer_from_server)


if __name__ == '__main__':
    client = Client()
    client.connect_to_server()

