import _thread
import time


class Producteur:

    def __init__(self, queue):
        self.queue = queue
        self.encore = True

    def start(self):
        _thread.start_new_thread(self.run, ())

    def stop(self):
        self.encore = False

    def run(self):
        i = 0
        with open('formations.csv', 'r+') as file:
            for line in file:
                arguments = line.split(";")
                formation = {"id": arguments[0], "name": arguments[1]}
                self.queue.put(formation)
                i += 1
                time.sleep(0.001)
