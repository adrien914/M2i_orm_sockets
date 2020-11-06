from consummer import Consummer
from client import Client
from queue import Queue


queue = Queue()

client = Client()
consummer = Consummer(client.qmain)

client.start()
consummer.start()
input()
client.stop()
consummer.stop()
