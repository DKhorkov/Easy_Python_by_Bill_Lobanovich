import string
import zmq
from time import sleep


class Publisher:

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port
        self.context = zmq.Context()
        self.server = self.context.socket(zmq.PUB)
        self.data = '''We have seen the Queen of cheese,
              Laying quietly at your ease,
              Gently fanned by evening breeze --
              Thy fair form no flies dare seize.

              All gaily dressed soon you'll go
              To the great Provincial Show,
              To be admired by many a beau
              In the city of Toronto.

              Cows numerous as a swarm of bees --
              Or as the leaves upon the trees --
              It did require to make thee please,
              And stand unrivalled Queen of Cheese.

              May you not receive a scar as
              We have heard that Mr. Harris
              Intends to send you off as far as
              The great World's show at Paris.

              Of the youth -- beware of these --
              For some of them might rudely squeeze
              And bite your cheek; then songs or glees
              We could not sing o' Queen of Cheese.

              We'rt thou suspended from baloon,
              You'd caste a shade, even at noon;
              Folks would think it was the moon
              About to fall and crush them soon.'''.split()  # Делаем список из песни

    def main(self):
        print(self.data)
        self.server.bind(f'tcp://{self.addr}:{self.port}')
        sleep(2)

        for word in self.data:
            word = word.strip(string.punctuation)  # Убираем знаки препинания
            print(word)
            if word.startswith(('a', 'i', 'u', 'e', 'o', 'A', 'I', 'O', 'U', 'E')):
                self.server.send_multipart(['Starts with vowel: '.encode('utf-8'), word.encode('utf-8')])
                print(word)
            if len(word) == 5:
                self.server.send_multipart(['Five letters in word: '.encode('utf-8'), word.encode('utf-8')])


if __name__ == '__main__':
    publisher = Publisher('127.0.0.1', 5555)
    publisher.main()
