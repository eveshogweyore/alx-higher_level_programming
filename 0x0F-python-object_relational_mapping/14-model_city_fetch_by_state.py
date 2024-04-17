#!/usr/bin/python3
"""Print all City objects from the database."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        join_result = (session.query(State, City)
                       .join(City, State.id == City.state_id)
                       .all()
                       )

        for state, city in join_result:
            print(f"{state.name}: ({city.id}) {city.name}")
