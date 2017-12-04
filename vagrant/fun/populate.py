from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rmfd_database_setup import City, Base, Person

engine = create_engine('sqlite:///rmfd.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Menu for UrbanBurger
city = City(name="Onesti")

session.add(city)
session.commit()

person = Person(name="Bogdan Radu", description=
       "Scurta descriere in care mentionez aspecte relevante legate de mine",
        city=city)

session.add(person)
session.commit()

person = Person(name="Constantin Radu", description=
       "Scurta descriere in care mentionez aspecte relevante legate de mine",
        city=city)

session.add(person)
session.commit()

person = Person(name="Dereck Radu", description=
       "Scurta descriere in care mentionez aspecte relevante legate de mine",
        city=city)

session.add(person)
session.commit()

person = Person(name="Emil Radu", description=
       "Scurta descriere in care mentionez aspecte relevante legate de mine",
        city=city)

session.add(person)
session.commit()

person = Person(name="Florian Radu", description=
       "Scurta descriere in care mentionez aspecte relevante legate de mine",
        city=city)

session.add(person)
session.commit()


print "added menu items!"
