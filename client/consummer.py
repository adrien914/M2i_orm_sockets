import _thread
import json
import time
from models import engine, Formation
from sqlalchemy.orm.session import sessionmaker


class Consummer:
    def __init__(self, queue):
        self.queue = queue
        self.keep_going = True


    def start(self):
        _thread.start_new_thread(self.run, ())

    def stop(self):
        self.keep_going = False

    def run(self):
        Session = sessionmaker(bind=engine)
        session = Session()

        while self.keep_going:
            if self.queue:
                formation = self.queue.get()
                print(formation)
                formation = json.loads(formation)
                session.add(Formation(formation["id"], formation["name"]))
                session.commit()
                print("Formation %s sauvegardée." % formation["name"])
            time.sleep(0.1)
        session.close()
