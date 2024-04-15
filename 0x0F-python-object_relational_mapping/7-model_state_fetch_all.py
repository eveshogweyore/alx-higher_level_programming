#!/usr/bin/python3
"""List all state objects from database."""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

session = Session()

states = session.query(State).all()

for state in states:
    print(f"{state.id}: {state.name}")

session.close()
