#import dependencies from SQLAlchemy & database_setup
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from rmfd_database_setup import Base, User
from random import randint
from datetime import date
#lets us know which DB engine we want to communicate with
engine = create_engine('sqlite:///rmfd.db')

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

''' Making new entries in the DB: '''

'''global gender
gender = 'n/a'

global url
url = 'http://2.bp.blogspot.com/-HzFJhEY3KtU/Tea7Ku92cpI/AAAAAAAAALw/uBMzwdFi_kA/s400/1.jpg'

global ocupation
ocupation = "Unknown"

global personality
personality = "Unknown"
global done'''
done = False

count = 0


def pick_gender(choice):
    if choice == 'm':
        gender = "male"
        url = 'http://4.bp.blogspot.com/-zsbDeAUd8aY/US7F0ta5d9I/AAAAAAAAEKY/UL2AAhHj6J8/s1600/facebook-default-no-profile-pic.jpg'
    elif choice == 'f':
        gender = "female"
        url = 'http://1.bp.blogspot.com/-jHrJ3VITQf8/UDILF_ctbOI/AAAAAAAACn4/UwOvDmW4EJw/s1600/CUTE+GIRL+HAIR+FB+DP.jpg'
    else:
         gender = "n/a"
         url = 'http://2.bp.blogspot.com/-HzFJhEY3KtU/Tea7Ku92cpI/AAAAAAAAALw/uBMzwdFi_kA/s400/1.jpg'
    return gender, url

def random_ocupation(nr_ocu):
    if nr_ocu == 0:
        ocupation = "Doctor"
    elif nr_ocu == 1:
         ocupation = "Fireman"
    elif nr_ocu == 2:
        ocupation = "Actor"
    elif nr_ocu == 3:
        ocupation = "Farmer"
    elif nr_ocu == 4:
        ocupation = "Writer"
    elif nr_ocu == 5:
        ocupation = "Painter"
    else:
        ocupation = "Musician"
    return ocupation

def random_temperament(nr_temp):
    if nr_temp == 0:
        personality = "Choleric"
    elif nr_temp == 1:
        personality = "Phlegmatic"
    elif nr_temp == 2:
        personality = "Sanguine"
    elif nr_temp == 3:
        personality = "Melancholic"
    return personality

def are_you_done(yesorno):
    if yesorno == 'y':
        done = True
    else:
        done = False
    return done

while done == False:
    print("Add a new user:")
    count += 1
    f_name = raw_input("first name: ")
    s_name = raw_input("second name: ")
    username = f_name+s_name+str(randint(0,99))
    password = 'admin123'
    email = f_name+'@'+s_name+'.com'
    dd = randint(1,27)
    mm = randint(1,12)
    yyyy = randint(1984,1999)
    dob = date(yyyy, mm, dd)
    choice = raw_input("gender ('m' or 'f'): ")
    print(choice)
    gender, url = pick_gender(choice)
    city = 'Springfield'
    description = 'This is a generic personal description. Here are my main traits'
    nr_ocu = randint(0,6)
    ocupation = random_ocupation(nr_ocu)
    nr_temp = randint(0,3)
    personality = random_temperament(nr_temp)
    tidyness = randint(0,100)
    guests = randint(0,100)


    newUser = User(username = username, password = password, f_name = f_name, s_name = s_name, email = email, dob = dob, gender = gender, city = city, description = description, ocupation = ocupation, tidyness = tidyness, guests = guests, personality = personality, url = url)

    session.add(newUser)
    session.commit()

    lastUser = session.query(User).filter_by(id=count)
    print(lastUser.all())

    yesorno = raw_input("are you done? (y/n)")
    done = are_you_done(yesorno)
