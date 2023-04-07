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
    addresses = relationship('Address',
                             back_populates='person',
                             order_by="Address.email",
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.name}(id={self.id})'


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship('Person', back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
anakin = Person(name='Anakin Skywalker', age=32)
obi1 = Person(name='Obi Wan Kenobi', age=40)
obi1.addresses = [
    Address(email='obi@example.com'),
    Address(email='wanwan@example.com')
]

session.add(anakin)
session.add(obi1)
session.commit()

an1 = session.query(Person).filter(
    Person.name.like('Ana%')
).first()
print(an1, an1.age, an1.name)
obi = session.query(Person).filter(
    Person.name.like('Obi%')
).first()
print(obi)
print(obi.addresses)
