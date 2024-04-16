#!/usr/bin/python3
"""Add the State object 'Louisiana' to the database."""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, Column
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        new_state = State(name='Louisiana')

        session.add(new_state)
        session.commit()

        print(new_state.id)
