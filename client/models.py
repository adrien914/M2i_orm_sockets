from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative.api import declarative_base

engine = create_engine("sqlite:///formations.db?check_same_thread=False", echo=True)
Base = declarative_base(engine)


class Formation(Base):
    __tablename__ = "cours"
    _id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, _id, name):
        self._id = _id
        self.name = name


Base.metadata.create_all()

