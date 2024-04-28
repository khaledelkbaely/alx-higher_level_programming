#!/usr/bin/python3
""" Creates the State California with the city san francisco
"""
from sys import argv
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).order_by(City.id)
    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.commit()
    session.close()
