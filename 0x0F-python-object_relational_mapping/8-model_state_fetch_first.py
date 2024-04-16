#!/usr/bin/python3
"""Print the first State object from database."""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).first()

    print(f"{state.id}: {state.name}")

    session.close()
