#import dependencies from SQLAlchemy & database_setup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

#lets us know which DB engine we want to communicate with
engine = create_engine('sqlite:///restaurantmenu.db')

'''binding the engine to the 'Base' class
this command makes the connections between our class definitions and the
coresponding tables within our DB'''
Base.metadata.bind = engine

'''this establishes a link of communication between our code executions and 
the engine we just created'''
DBSession = sessionmaker(bind = engine)

''' from now on, when I want to make a change to the DB, I can do it just by
calling a method from within session;
the DBSession object gives me a staging zone for all of the objects loaded into
the DBSession object;
any change made to the objects in the session won't be persisted into the DB 
untill I call session.commit'''
session = DBSession()

session.query(Restaurant).all()