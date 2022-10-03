import datetime
from xmlrpc.server import SimpleXMLRPCServer


class Server:

    def __init__(self, addr, port):
        self.addr = addr
        self.port = port

    def current_time(self):
        return str(datetime.datetime.now())

    def unknown_command(self):
        return 'Unknown command, try again'

    def run_server(self):
        self.server = SimpleXMLRPCServer((self.addr, self.port))
        self.server.register_function(self.current_time, 'current_time')
        self.server.register_function(self.unknown_command, 'unknown_command')
        print('server is runnig')
        self.server.serve_forever()


if __name__ == '__main__':
    server = Server("localhost", 5001)
    server.run_server()
