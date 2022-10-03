import zmq


class Subscriber:

    def __init__(self, addr, port, topic_for_sub):
        self.addr = addr
        self.port = port
        self.topic = topic_for_sub
        self.context = zmq.Context()
        self.client = self.context.socket(zmq.SUB)

    def main(self):
        self.client.connect(f'tcp://{self.addr}:{self.port}')
        self.client.setsockopt(zmq.SUBSCRIBE, self.topic.encode('utf-8'))

        while True:
            self.topic, self.word = self.client.recv_multipart()
            print(self.topic.decode('utf-8'), self.word.decode('utf-8'))


if __name__ == '__main__':
    # subscriber = Subscriber('127.0.0.1', 5555, 'Starts with vowel: ')
    # subscriber.main()

    subscriber_2 = Subscriber('127.0.0.1', 5555, 'Five letters in word: ')
    subscriber_2.main()
