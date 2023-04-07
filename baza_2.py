from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
anakin = Person(name='Anakin Skywalker', age=32)
session.add(anakin)
session.commit()

an1 = session.query(Person).filter(
    Person.name.like('Ana%')
).first()
print(an1, an1.age, an1.name)
