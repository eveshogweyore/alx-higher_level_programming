#!/usr/bin/python3
"""Change the name of a State object from the database."""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = session.query(State).filter_by(id=2)

        state[0].name = "New Mexico"

        session.commit()
