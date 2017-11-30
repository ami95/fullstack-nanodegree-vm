import sys
from sqlalchemy import Column, ForeignKey, Integer, String
'''used in the config and class code '''
from sqlalchemy.ext.declarative import declarative_base
'''create our fk-relationships & lso used when we write our mapper '''
from sqlalchemy.orm import relationship
'''used 4 config code @ the end of this file''' 
from sqlalchemy import create_engine

'''lets sqlalchemy know that our classes are special sqlalchemy classes that 
corespond to tables in our DB''' 
Base = declarative_base() 


class Restaurant(Base):

	__tablename__ = 'restaurant'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)


class MenuItem(Base):

	__tablename__ = 'menu_item'

	name = Column(String(80), nullable = False)
	id = Column(Integer, primary_key = True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	'''look inside the restaurant table and retrieve the id nr. 
	whenever I ask for restaurant_id '''
	restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
	restaurant = relationship(Restaurant)

	@property
	def serialize(self):
		#Returns object data in easy serializable format
		return{
			'name' : self.name,
			'description' : self.description,
			'id' : self.id,
			'price' : self.price,
			'course' : self.course,
			}


'''point to the DB we will use & creates new .db file'''
engine = create_engine('sqlite:///restaurantmenu.db')

'''goes into the DB and adds tha classes we will soon create, as new tables'''
Base.metadata.create_all(engine)