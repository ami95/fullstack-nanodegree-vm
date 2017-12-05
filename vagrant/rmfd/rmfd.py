from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from rmfd_database_setup import Base, User

app = Flask(__name__)

engine = create_engine('sqlite:///rmfd.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/login')
def renderLoginPage():
	output = "This page displays the login form"
	return render_template('login.html')

@app.route('/inregistrare/')
def renderSignUpPage():
	output = "This page displays the sign-up form"
	return render_template('signup.html')

@app.route('/profilul_meu/')
def renderMyProfile():
	output = "This page displays the logged in users profile"
	return render_template('myprofile.html', user = user)

@app.route('/profilul_meu/editare')
def editMyProfile():
	output = "On this page you can edit the logged in users profile"
	return render_template('editmyprofile.html', user = user)

@app.route('/cauta')
def filterSearch():
	output = "On this site you can search a new roommate, using filter criteria"
	return render_template("search.html", users = users)

@app.route('/user/<int:user_id>')
def renderUserProfile(user_id):
	output = "On this site you can check another users profile"
	return render_template('userprofile.html', user2 = user2, user = user)

if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port=5000)






"""
user = {"id": "1", "username": "homers", "f_name":"Homer", "s_name":"Simpson", "email": "homer@simpson.com", "dob":"01-02-1952", "gender":"male", "city":"Springfield", "description": "Homer Jay Simpson is a fictional character and the main protagonist of the American animated television series The Simpsons as the patriarch of the eponymous family. He is voiced by Dan Castellaneta and first appeared on television, along with the rest of his family, in The Tracey Ullman Show short 'Good Night' on April 19, 1987.", "ocupation":"Safety Inspector at the Nuclear Power Plant", "tidyness":"8", "guests":"30", "personality":"choleric", "url":"http://assets.nydailynews.com/polopoly_fs/1.1344824.1368642299!/img/httpImage/image.jpg_gen/derivatives/article_970/ford-homer-simpson.jpg"}

user2 = {"id": "4", "username": "marges", "f_name":"Marge", "s_name":"Simpson", "email": "marge@simpson.com", "dob":"01-08-1955", "gender":"female", "city":"Springfield",
		"description": "Marjorie Jacqueline 'Marge' Simpson is a fictional character in the American animated sitcom The Simpsons and part of the eponymous family. She is voiced by Julie Kavner and first appeared on television in The Tracey Ullman Show short 'Good Night' on April 19, 1987", "ocupation":"Housewife ", "tidyness":"98", "guests":"70", "personality":"sangvinic", "url":"https://kalindamage.files.wordpress.com/2014/06/margesimpson5.gif"}


users = [{"id": "1", "username": "homers", "f_name":"Homer", "s_name":"Simpson", "email": "homer@simpson.com", "dob":"01-02-1952", "gender":"male", "city":"Springfield",
"description": "Homer Jay Simpson is a fictional character and the main protagonist of the American animated television series The Simpsons as the patriarch of the eponymous family. He is voiced by Dan Castellaneta and first appeared on television, along with the rest of his family, in The Tracey Ullman Show short 'Good Night' on April 19, 1987.", "ocupation":"Safety Inspector at the Nuclear Power Plant", "tidyness":"8", "guests":"30", "personality":"choleric", "url":"http://assets.nydailynews.com/polopoly_fs/1.1344824.1368642299!/img/httpImage/image.jpg_gen/derivatives/article_970/ford-homer-simpson.jpg"},
		{"id": "2", "username": "moes", "f_name":"Moe", "s_name":"Szyslak", "email": "moe@szyslak.com", "dob":"21-04-1948", "gender":"male", "city":"Springfield",
		"description": "Morris Moe or Moh Szyslak is a fictional character from the American animated television series The Simpsons. He is voiced by Hank Azaria and first appeared in the series premiere episode 'Simpsons Roasting on an Open Fire'.", "ocupation":"Proprietor of Moe's Tavern", "tidyness":"2", "guests":"4", "personality":"melancholic", "url":"https://peopledotcom.files.wordpress.com/2016/08/moe-600x450.jpg?w=600&h=450"},
		{"id": "3", "username": "burnsm", "f_name":"Montgomery", "s_name":"Burns", "email": "monty@burns.com", "dob":"06-06-1832", "gender":"male", "city":"Springfield",
		"description": "Charles Montgomery Burns, known as C. Montgomery Burns and Monty Burns, but usually referred to simply as Mr. Burns, is a recurring character in the animated television series The Simpsons, and is voiced by Harry Shearer. Mr. Burns is the evil owner of the Springfield Nuclear Power Plant and is also HomerSimpson's boss. He is assisted at almost all times by Waylon Smithers, his loyal and sycophantic aide, adviser, confidant and secret admirer.", "ocupation":"Owner of the Springfield Nuclear Power Plant", "tidyness":"81", "guests":"1", "personality":"sangvinic", "url":"http://www.imaginaryeric.com/wp-content/uploads/2009/04/burns.jpg"},
		{"id": "4", "username": "marges", "f_name":"Marge", "s_name":"Simpson", "email": "marge@simpson.com", "dob":"01-08-1955", "gender":"female", "city":"Springfield",
		"description": "Marjorie Jacqueline 'Marge' Simpson is a fictional character in the American animated sitcom The Simpsons and part of the eponymous family. She is voiced by Julie Kavner and first appeared on television in The Tracey Ullman Show short 'Good Night' on April 19, 1987", "ocupation":"Housewife ", "tidyness":"98", "guests":"70", "personality":"sangvinic", "url":"https://kalindamage.files.wordpress.com/2014/06/margesimpson5.gif"}]
"""
