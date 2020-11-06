import socket, _thread, queue


class Client:
    def __init__(self):
        self.exchange_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.qmain = queue.Queue()
        self.keep_going = True

    def start(self):
        _thread.start_new_thread(self.exchange, ())

    def stop(self):
        self.keep_going = False

    def exchange(self):
        self.exchange_socket.connect(('localhost', 2222))
        buffer = b""
        while self.keep_going:
            buffer += self.exchange_socket.recv(100)
            print("buffer:", buffer)
            formation = buffer.decode().split("\n")
            print("formation:", formation)
            for formation in formation[:-1]:
                self.qmain.put(formation)
            # buffer = formation[-1].encode()
            buffer = b""
        self.exchange_socket.close()
