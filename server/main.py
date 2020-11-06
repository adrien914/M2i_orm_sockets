from ecoute import Ecoute
from producteur import Producteur
from queue import Queue


queue = Queue()

ecoute = Ecoute(queue)
producteur = Producteur(queue)

ecoute.start()
producteur.start()
input()
ecoute.stop()
producteur.stop()
