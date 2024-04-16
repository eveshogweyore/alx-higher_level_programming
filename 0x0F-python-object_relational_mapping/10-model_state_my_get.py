#!/usr/bin/python3
"""Print the State object with the name passed as argument."""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine, Column
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"

    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)

    with Session() as session:
        state = (session
                 .query(State)
                 .filter(Column('name').like(argv[4]))
                 .all()
                 )

    if state:
        print(state[0].id)
    else:
        print("Not found")
