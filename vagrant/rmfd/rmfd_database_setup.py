import sys
from sqlalchemy import Column, ForeignKey, Integer, String
'''used in the config and class code '''
from sqlalchemy.ext.declarative import declarative_base
'''create our fk-relationships & lso used when we write our mapper '''
from sqlalchemy.orm import relationship
'''used 4 config code @ the end of this file'''
from sqlalchemy import create_engine
from sqlalchemy.types import Date

'''lets sqlalchemy know that our classes are special sqlalchemy classes that
corespond to tables in our DB'''
Base = declarative_base()



class User(Base):

    __tablename__ = 'user'

    username = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    password = Column(String(16))
    f_name = Column(String(80), nullable = False)
    s_name = Column(String(80), nullable = False)
    email = Column(String(80))
    dob = Column(Date)
    gender = Column(String(6))
    city = Column(String(80))
    description = Column(String(300))
    ocupation = Column(String(80))
    tidyness = Column(Integer)
    guests = Column(Integer)
    personality = Column(String(12))
    url = Column(String(800))



#### End of File ####
'''point to the DB we will use & creates new .db file'''
engine = create_engine('sqlite:///rmfd.db')

'''goes into the DB and adds tha classes we will soon create, as new tables'''
Base.metadata.create_all(engine)
