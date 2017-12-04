import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import date

Base = declarative_base()

class City(Base):
	__tablename__ = 'city'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)

class Person(Base):
	
	__tablename__ = 'person'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	#dob = Column(Date)
	description = Column(String(340))
	city_id = Column(Integer, ForeignKey('city.id'))
	city = relationship(City)
'''
	def calculate_age(dob):
    today = date.today()
    return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
	age = Column(calculate_age(dob))
'''
### end of file ###
engine = create_engine('sqlite:///rmfd.db')
Base.metadata.create_all(engine)

