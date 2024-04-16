#!/usr/bin/python3
"""Delete all State objects with a name containing the letter a."""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, Column
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(db_url)

    Session = sessionmaker(engine)

    with Session() as session:
        states = (session
                  .query(State)
                  .filter(Column('name').like('%a%'))
                  )

        for state in states:
            session.delete(state)

        session.commit()
